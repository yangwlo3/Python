from datetime import datetime


name = input("Enter your name: ")
gender = input("Enter your gender: ")
print(gender)

def get_Time(dt_object):
    

    if dt_object.hour < 12:
        return "Morning"
    else:
        return "Afternoon"
    
    
date_time = datetime.now()

day = get_Time(date_time)
morning_time = datetime(2025, 8, 8, 14, 30, 0)

print(f"Hello {name} {get_Time(morning_time)}.")