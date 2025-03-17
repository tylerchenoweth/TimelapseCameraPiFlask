
# For the camera stream
from app import picam2 
import cv2

# For the pi stats
import psutil
import os
import time

import json

from datetime import datetime



def generate_frames():

    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# For the Pi stats
def get_cpu_temp():
    """Get CPU temperature."""
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        clean_temp = temp.replace("'C", "").strip()

        return clean_temp.replace("temp=", "").strip()
    except:
        return "N/A"


def get_cpu_usage():
    """Get CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_ram_usage():
    """Get RAM usage and total memory in MB."""
    ram = psutil.virtual_memory()
    used = ram.used // (1024 * 1024)  # Convert to MB
    total = ram.total // (1024 * 1024)  # Convert to MB

    return used, total


def get_disk_usage():
    """Get disk usage and total storage in GB."""
    disk = psutil.disk_usage('/')
    used = disk.used // (1024 ** 3)  # Convert to GB
    total = disk.total // (1024 ** 3)  # Convert to GB
    return used, total



def get_display_stats():

    cpu_temp = get_cpu_temp()
    cpu_usage = get_cpu_usage()
    ram_usage, ram_total = get_ram_usage()
    disk_usage, disk_total = get_disk_usage()

    context = {
        "cpu_temp" : cpu_temp,
        "cpu_usage" : cpu_usage,
        "ram_usage" : ram_usage,
        "disk_usage" : disk_usage,

        "ram_total": ram_total,
        "disk_total": disk_total,
    }

    yield f"data: {json.dumps(context)}\n\n"

    time.sleep(1)





def getTime():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") 


def fuck():
    # os.system("clear")
    print("Making folder for images...")
    allTimelapses = "Timelapses"
    timelapseFolder = getTime()

    os.makedirs(allTimelapses, exist_ok=True)
    os.makedirs(f"{allTimelapses}/{timelapseFolder}", exist_ok=True)

    counter = 0

    while True:
        
        picam2.capture_file(f"./{allTimelapses}/{timelapseFolder}/timelapse_{counter}.jpg")  # Capture and save an image
        print(f"Image saved as {counter}.jpg")
        counter += 1
        
        time.sleep(5)









# OLD LOGGER CLASS FOR DISPLAYING STATS AT THE BOTTOM


# # Store the last 10 log terminal
# log_messages = []

# class LimitedLogHandler(logging.StreamHandler):
#     def display_logs(self):
#         """Clears the terminal and displays the 10 most recent logs, keeping the persistent text below."""
#         sys.stdout.write("\033c")  # Clear screen
#         sys.stdout.write("Recent Logs:\n")
#         sys.stdout.write("\n".join(log_messages) + "\n")
        
#         sys.stdout.write("THe bottom...\n\n")

#         sys.stdout.flush()
        
#     def emit(self, record):
#         global log_messages
#         log_messages.append(self.format(record))
#         if len(log_messages) > 10:
#             log_messages.pop(0)
#         self.display_logs()

 
# # # Set up Flask logging
# log_handler = LimitedLogHandler()
# log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
# app.logger.addHandler(log_handler)
# app.logger.setLevel(logging.INFO)