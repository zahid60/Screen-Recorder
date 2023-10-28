import cv2
import pyautogui
import numpy as np
import time

# Get screen width and height
screen_width, screen_height = pyautogui.size()

# Define the output video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("screen_recording.mp4", fourcc, 24.0, (screen_width, screen_height))

# Prompt the user to specify the recording duration
duration = int(input("Enter the recording duration in seconds: "))

start_time = time.time()
end_time = start_time + duration

try:
    while time.time() < end_time:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)

        # Convert the screenshot to BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video
        output.write(frame)

    print("Recording completed.")
except KeyboardInterrupt:
    print("Recording interrupted.")

# Release the VideoWriter and close the output file
output.release()
