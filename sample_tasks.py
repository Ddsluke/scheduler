import time
from datetime import datetime

def sleep(sec):
    print(f"Timer started. Expected time {sec} seconds.")
    time.sleep(sec)
    print(f"Slept for {sec} seconds.")

def clock():
    print("The time is %s"%datetime.now())

if __name__ == "__main__":
    sleep(3600)