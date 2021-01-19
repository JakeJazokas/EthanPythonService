import argparse
import sched
import time
import ctypes

#TO RUN THIS FILE USE: python BackgroundFitnessScript.py -i <TIME_IN_SECONDS>
#TO RUN THIS FILE IN THE BACKGROUND USE: pythonw BackgroundFitnessScript.py -i <TIME_IN_SECONDS>

parser = argparse.ArgumentParser(description='Arguments for the fitness script.')

parser.add_argument('-i', '--interval', type=int, help='The time in seconds between notifications.', required=True)

args = parser.parse_args()

s = sched.scheduler(time.time, time.sleep)

def create_messagebox(sc): 
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
    s.enter(args.interval, 1, create_messagebox, (sc,))

s.enter(args.interval, 1, create_messagebox, (s,))
s.run()
