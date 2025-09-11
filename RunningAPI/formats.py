# series of functions for converting or formatting data 

import math

def nearest_whole_km(Distance: float):
    DistanceInt = int(Distance)
    DistacneNearest = round(DistanceInt / 1000)
    
    return DistacneNearest

def convert_to_km(Distance: float):
    Distance = Distance/1000
    
    return Distance

def convert_from_mins(Time: float):
    # converts time stored as minutes to hh:mm:ss FOR DISPLAY
    Hours = int(Time // 60)
    Minutes = int(Time % 60)
    Seconds = int(math.modf(Time)[0] * 60)
    
    return f'{Hours:02d}:{Minutes:02d}:{Seconds:02d}'

def calculate_pace(Distance: float, Time: int):
    # calculate a pace in min/km for a given distance(km) and time(min) FOR DISPLAY
    Pace = math.modf(Time/Distance)

    Minutes = int(Pace[1])
    Seconds = int(Pace[0] * 60)
    
    return f'{Minutes}:{Seconds:02d}/km'

def convert_decimnal_pace(Pace: float):
    # converts pace in a decimal format into min/km FOR DISPLAY
    Pace = math.modf(Pace)

    Minutes = int(Pace[1])
    Seconds = int(Pace[0] * 60)
    
    return f'{Minutes}:{Seconds:02d}/km'

def round_distance_str(distance: float):
    # rounds a distance and adds km (returns as string) FOR DISPLAY
    Distance = round(distance, 2)
    
    return f'{Distance} km' 

def round_distance(distance: float):
    # rounds a distance and adds km (returns as string) FOR DISPLAY
    Distance = round(distance, 2)
    
    return Distance 