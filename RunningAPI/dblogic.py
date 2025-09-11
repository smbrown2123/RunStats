import psycopg
import json
from datetime import datetime

def write_runs_to_db(runs: list):
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    runs.reverse()  
    for i in range(0, len(runs)):
        data = runs[i]
        pace = float(data['pace'])
        distance = float(data['distance'])
        duration = float(data['time'])
        strdate = str(data['date'])
        date = datetime.strptime(strdate, "%d-%m-%Y").date()

        # Connect to an existing database
        with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                # Pass data to fill a query placeholders and let Psycopg perform
                # the correct conversion (no SQL injections!)
                cur.execute(
                    "INSERT INTO run (pace, distance, duration, date) VALUES (%s, %s, %s, %s)",
                    (pace, distance, duration, date))

                # Make the changes to the database persistent
                conn.commit()
      
def get_all_runs_from_db():
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    data = ''
    
    with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT json_agg(json_build_object('id', public.run.id,'pace', public.run.pace,'duration', public.run.duration,'distance', public.run.distance,'date', public.run.date)) FROM public.run;")
                result = cur.fetchone()
                data = result[0] 
    return data

def get_run_from_db_by_id(run_id):
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    data =[]
    
    with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM run where id= (%s)",(run_id,))
                for record in cur:
                    data.append(record)
                   
    return data

def count_runs_in_db():
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]
    
    with psycopg.connect(dbname = dbname, 
                                user = user, 
                                host= host,
                                password = password,
                                port = port ) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                cur.execute("SELECT count(*) FROM run ")
                result = cur.fetchone()
                
    return result[0]

def clear_runs():
    params = get_db_parameters()
    dbname = params[0]
    user = params[1]
    host = params[2]
    password = params[3]
    port = params[4]

    # Connect to an existing database
    with psycopg.connect(dbname = dbname, 
                            user = user, 
                            host= host,
                            password = password,
                            port = port ) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute(
                "TRUNCATE run; DELETE FROM run")

            # Make the changes to the database persistent
            conn.commit()

def get_db_parameters():
    with open('dbparams.json') as f:
        params = json.load(f)

    dbname = params["parameters"]["dbname"]
    user = params["parameters"]["user"]
    host = params["parameters"]["host"]
    password = params["parameters"]["password"]
    port = params["parameters"]["port"]
    
    return dbname, user, host, password, port