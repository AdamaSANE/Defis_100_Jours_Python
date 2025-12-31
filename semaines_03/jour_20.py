# Event Coundown Timer
import time
from datetime import datetime, timedelta

# Step 1: Get Event Date and Time from User
def get_event_datetime():
  try:
    event_date_str = input("Enter the event date and time (YYYY-MM-DD HH:MM:SS): ")
    event_datetime = datetime.strptime(event_date_str, "%Y-%m-%d %H:%M:%S")
    return event_datetime
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
    return None
  
# Step 2: Calculate Time Remaining
def calculate_time_remaining(event_datetime):
  current_time = datetime.now()
  return event_datetime - current_time

# Step 3: Display Countdown Timer
def display_countdown(time_left):
  days = time_left.days
  hours, remainder = divmod(time_left.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  print(f"\nTime remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end='')

# Step 4: Main Countdown Loop
def countdown_timer(event_date):
  while True:
    time_left = calculate_time_remaining(event_date)
    if time_left.total_seconds() <= 0:
      print("\nCountdown complete!")
      break
    display_countdown(time_left)
    time.sleep(1)

# Main Program
event_datetime = get_event_datetime()
if event_datetime:
  print(f"Event set for: {event_datetime}")
  countdown_timer(event_datetime)