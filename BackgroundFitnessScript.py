import argparse
import sched
import time
import ctypes
from random import randrange

#TO RUN THIS FILE USE: python BackgroundFitnessScript.py -i <TIME_IN_SECONDS>
#TO RUN THIS FILE IN THE BACKGROUND USE: pythonw BackgroundFitnessScript.py -i <TIME_IN_SECONDS>

workout_titles = [
    "Standing Hamstring Stretch",
    "Piriformis Stretch",
    "Lunge With Spinal Twist"
    ]

workout_descriptions = [
    "Stand tall with your feet hip-width apart, knees slightly bent, arms by your sides...",
    "Sit on the floor with both legs extended in front of you...",
    "Start standing with your feet together..."
    ]

parser = argparse.ArgumentParser(description='Arguments for the fitness script.')

parser.add_argument('-i', '--interval', type=int, help='The time in seconds between notifications.', required=True)

args = parser.parse_args()

s = sched.scheduler(time.time, time.sleep)

def create_messagebox(sc):
    random_index = randrange(len(workout_titles))
    ctypes.windll.user32.MessageBoxW(0, workout_descriptions[random_index], workout_titles[random_index], 1)
    s.enter(args.interval, 1, create_messagebox, (sc,))

s.enter(args.interval, 1, create_messagebox, (s,))
s.run()
