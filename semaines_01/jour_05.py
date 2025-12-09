# Countdown Timer

import time

# Step 1: Get user input for the countdown start
start = int(input("Enter the number to start for the countdown from: "))

# Step 2: Countdown using a while loop
print("\n==== Countdown Begins ====")
while start >= 0:
    print(start)
    time.sleep(1)  # Pause for 1 second
    start -= 1

# Step 3: Print finale message
print("\n====Countdown Complete!====")