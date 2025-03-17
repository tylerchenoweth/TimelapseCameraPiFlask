from flask import Flask, Response
import logging
import sys
import time
import threading



# For the Pi stats
import psutil
import os
import time

from datetime import datetime



from picamera2 import Picamera2

picam2 = Picamera2()  # Initialize camera
picam2.start()



app = Flask(__name__)

import routes
# from timelapse import fuck
from utils import fuck

# def getTime():
#     return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") 


# def fuck():
#     os.system("clear")
#     print("Making folder for images...")
#     folderName = getTime()
#     os.makedirs(folderName, exist_ok=True)


#     # picam2 = Picamera2()  # Initialize camera
#     # picam2.start()  # Start the camera

#     counter = 0
#     print("\n\n\n\n\n\n\n HELLO \n\n\n\n\n\n\n\n")

#     while True:
        
#         picam2.capture_file(f"./{folderName}/timelapse_{counter}.jpg")  # Capture and save an image
#         print(f"Image saved as {counter}.jpg")
#         counter += 1
        
#         time.sleep(5)



def start_background_thread():
    """Start the background thread if it's not already running."""
    thread = threading.Thread(target=fuck, daemon=True)
    thread.start()


# Start the background thread when the module is imported
start_background_thread() 


if __name__ == '__main__':
    

    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000, )
    

 


