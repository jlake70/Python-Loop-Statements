# Task 1

moods = ["Happy", "Sad", "Energetic", "Calm" ]

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

times_of_day = ["Morning", "Afternoon", "Evening"]

import random

for day in days_of_week:
    print(f"Moods for {day}: ")

    for time in times_of_day:
        mood = random.choice(moods)
        print(f" {time} : {mood}")
