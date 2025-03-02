from picamera2 import Picamera2
from datetime import datetime
import time
import os

def getTime():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") 

os.system("clear")
print("Making folder for images...")
folderName = getTime()
os.makedirs(folderName, exist_ok=True)


picam2 = Picamera2()  # Initialize camera
picam2.start()  # Start the camera

counter = 0

while True:
    
    picam2.capture_file(f"./{folderName}/timelapse_{counter}.jpg")  # Capture and save an image
    print(f"Image saved as {counter}.jpg")
    counter += 1
    
    time.sleep(5)


