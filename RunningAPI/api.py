from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from RunningAPI.dblogic import *
from RunningAPI.running import *

RunningAPI = FastAPI()

origins = [
    "http://localhost:3000"
]

RunningAPI.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@RunningAPI.get("/runs")
def all_runs():
    response = get_all_runs_from_db()
    
    return response

@RunningAPI.get("/run/{run_id}")
def get_run_by_id(run_id):
    response = get_run_from_db_by_id(run_id)
    
    return response

@RunningAPI.get("/runs/refresh")
def refresh_data_from_strava():
    runsDb = count_runs_in_db()
    runs = get_new_runs(runsDb)
    write_runs_to_db(runs)
    
    return f"Db data refreshed with {len(runs)} new runs."

@RunningAPI.get("/runs/hard-refresh")
def refresh_all_runs_from_strava():
    clear_runs()
    runs = get_runs()
    write_runs_to_db(runs)
    
    return f"Database hard refreshed with {len(runs)} runs."