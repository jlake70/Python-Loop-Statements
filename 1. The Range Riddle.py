# Task 1

moods = ["Happy", "Sad", "Energetic", "Calm" ]

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

import random

for day in days_of_week:
 
    mood = random.choice(moods)
    print(f"On {day}" + f" mood is: {mood} ")