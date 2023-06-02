import time

"""
Version: 1.2
Author: Michael Raheem
Name: Workout Routine
Desc: Script for a daily workout session
"""

routine_file = "routine.txt"  # Path to the external routine file
duration = int(input("Enter the start time per routine in seconds (e.g., 45): "))
rest = duration // 3  # resting time

with open(routine_file, "r") as file:
    routine = file.read().splitlines()

for index, exercise in enumerate(routine):
    print(f"Countdown started for {exercise}")
    time.sleep(1)

    for i in range(duration, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)

    if index < len(routine) - 1:
        print(f"{rest} seconds rest \nGet in position for {routine[index + 1]}")
    else:
        print("Great Workout Today! \nSee you tomorrow")

    time.sleep(rest)
