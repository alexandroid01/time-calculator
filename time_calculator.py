# time calculator exercise from https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

import math

def add_time(start, duration, day):
    # separate the hour and the minutes in the start and duration variables
    start = start.split(" ")
    am_or_pm = start[1]

    start_split = start[0].split(":")
    start_hours = int(start_split[0])
    start_minutes = int(start_split[1])

    duration_split = duration.split(":")
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[1])

    # assign a numerical value to each day of the week
    day = day.lower()
    start_day = 0
    if day == "sunday":
        start_day = 0
    elif day == "monday":
        start_day = 1
    elif day == "tuesday":
        start_day = 2
    elif day == "wednesday":
        start_day = 3
    elif day == "thursday":
        start_day = 4
    elif day == "friday":
        start_day = 5
    elif day == "saturday":
        start_day = 6

    # change into military time for ease of calculation
    if am_or_pm == "PM" and start_hours < 12:
        start_hours = start_hours + 12
    if am_or_pm == "AM" and start_hours == 12:
        start_hours = 0

    # add the start_hours + duration_hours, and the start_minutes + duration_minutes
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes

    # carry over the minutes into hours, if applicable
    if start_minutes + duration_minutes >= 60:
        new_minutes = new_minutes - 60
        new_hours = new_hours + 1 

    # calculate how many days fit into the new hours
    number_days = math.trunc(new_hours / 24)
    new_hours = new_hours - (24 * number_days)
   
    # change back into 12-hour time
    if new_hours >= 12:
        am_or_pm = "PM"
        if new_hours > 12:
            new_hours = new_hours - 12
    else:
        am_or_pm = "AM"
    
    if new_hours == 0:
        new_hours = 12
    
    # if new_minutes is a single-digit integer, format new_minutes to display a zero before the digit
    if new_minutes < 10:
        new_minutes = str(new_minutes).zfill(2)  

    # determine what message to print for number of days later
    if number_days == 0:
        days_later = "same day"
    elif number_days == 1:
        days_later = "next day"
    else:
        days_later = str(number_days) + " days later"

    # create a list of the days of the week
    days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    # calculate the new day of the week
    if number_days >= 7:
        number_days = number_days % 7
    
    new_day = start_day + number_days
    if new_day >= 7:
        new_day = new_day - 7
    
    new_day = days_of_week[new_day]


    # print new calculated time
    print("--------")
    print(f"Calculated Time: {new_hours}:{new_minutes} {am_or_pm} on {new_day} ({days_later})")

# beginning of program 
user_start = input("Enter the start time: ")
user_duration = input("Enter the duration time: ")
user_day = input("Enter the day of the week: ")

add_time(user_start, user_duration, user_day)
