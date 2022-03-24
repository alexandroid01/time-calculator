# time calculator exercise from https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

    # a start time in the 12-hour clock format (ending in AM or PM)
    # a duration time that indicates the number of hours and minutes
    # (optional) a starting day of the week, case insensitive
    # The function should add the duration time to the start time and return the result.
    # If the result will be the next day, it should show (next day) after the time. 
    # If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

def add_time(start, duration):
    # step 1: separate the hour and the minutes in the start and duration variables
    start = start.split(" ")
    am_or_pm = start[1]

    start_split = start[0].split(":")
    start_hours = int(start_split[0])
    start_minutes = int(start_split[1])

    duration_split = duration.split(":")
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[1])

    # step 2: add the start_hours + duration_hours, and the start_minutes + duration_minutes
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes
    
    # step 3: carry over minutes into hours
    if new_minutes >= 60:
        new_minutes = new_minutes - 60
        new_hours = new_hours + 1 

    # step 4: format new_minutes if result is a single-digit integer
    if new_minutes < 10:
        new_minutes = str(new_minutes).zfill(2)  
    
    print(new_hours)
    print(new_minutes)

    # step 5: figure out how to deal with the AM and PM situation, and carrying over into the next day
    # ^maybe start with 24-hour time and then figure out how to convert?

add_time("2:02 PM", "1:03")

