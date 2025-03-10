from flask import Flask, Response
import logging
import sys
import time
import threading



# For the Pi stats
import psutil
import os
import time

import datetime

from timelapse import fuck

from picamera2 import Picamera2



picam2 = Picamera2()
picam2.start()

app = Flask(__name__)

import routes

# For the Pi stats
def get_cpu_temp():
    """Get CPU temperature."""
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        clean_temp = temp.replace("'C", "").strip()
        # print(f"***\n\n\n{temp}\n\n\n*****")
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


def display_stats():

    # Run forever
    while True:

        # Get all stats
        cpu_temp = get_cpu_temp()
        cpu_usage = get_cpu_usage()
        ram_used, ram_total = get_ram_usage()
        disk_used, disk_total = get_disk_usage()

        ranges = ["🟢", "🟡", "🟠", "🔴"]

        cpu_temp_status = ""
        cpu_usage_status = ""
        ram_usage_status = ""
        disk_usage_status = ""

        if(float(cpu_temp) <= 50):
            cpu_temp_status = ranges[0]
        elif(float(cpu_temp) <= 70):
            cpu_temp_status = ranges[1]
        elif(float(cpu_temp) <= 80):
            cpu_temp_status = ranges[2]
        else:
            cpu_temp_status = ranges[3]

        if(float(cpu_usage) <= 5):
            cpu_usage_status = ranges[0]
        elif(float(cpu_usage) <= 30):
            cpu_usage_status = ranges[1]
        elif(float(cpu_usage) <= 70):
            cpu_usage_status = ranges[2]
        else:
            cpu_usage_status = ranges[3]


        if(float(ram_used) <= 250):
            ram_usage_status = ranges[0]
        elif(float(ram_used) <= 500):
            ram_usage_status = ranges[1]
        elif(float(ram_used) <= 750):
            ram_usage_status = ranges[2]
        else:
            ram_usage_status = ranges[3]


        if(float(disk_used) <= 13):
            disk_usage_status = ranges[0]
        elif(float(disk_used) <= 20):
            disk_usage_status = ranges[1]
        elif(float(disk_used) <= 25):
            disk_usage_status = ranges[2]
        else:
            disk_usage_status = ranges[3]

        

        # Print stats
        sys.stdout.write(f"{'='*30}\n")
        sys.stdout.write(" 🖥️ Raspberry Pi System Stats \n")
        sys.stdout.write(f"{'='*30}\n")
        sys.stdout.write(f"🌡️  CPU Temperature  : {cpu_temp_status} {cpu_temp}\n")
        sys.stdout.write(f"⚙️  CPU Usage        : {cpu_usage_status} {cpu_usage}%\n")
        sys.stdout.write(f"💾 RAM Usage        : {ram_usage_status} {ram_used}MB / {ram_total}MB\n")
        sys.stdout.write(f"📂 Disk Usage       : {disk_usage_status} {disk_used}GB / {disk_total}GB\n")
        sys.stdout.write(f"{'='*30}\n")

        time.sleep(.5)

        # Hop back 8 lines to overwrite them
        for _ in range(8):
            sys.stdout.write("\033[F\033[K")






# Store the last 10 log terminal
log_messages = []

class LimitedLogHandler(logging.StreamHandler):
    def display_logs(self):
        """Clears the terminal and displays the 10 most recent logs, keeping the persistent text below."""
        sys.stdout.write("\033c")  # Clear screen
        sys.stdout.write("Recent Logs:\n")
        sys.stdout.write("\n".join(log_messages) + "\n")
        
        sys.stdout.write("THe bottom...\n\n")

        sys.stdout.flush()
        
    def emit(self, record):
        global log_messages
        log_messages.append(self.format(record))
        if len(log_messages) > 10:
            log_messages.pop(0)
        self.display_logs()

    

        



# # Set up Flask logging
log_handler = LimitedLogHandler()
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)


from datetime import datetime

def getTime():
    return datetime.now().strftime("%Y-%m-%d_%H:%M:%S") 


def fuck():

    app.logger.info("Starting timelapse camera...")
    # print("Making folder for images...")
    app.logger.info("Making folder for images...")
    # time.sleep(5)
    folderName = getTime()
    os.makedirs(folderName, exist_ok=True)


    # picam2 = Picamera2()  # Initialize camera
    # picam2.start()  # Start the camera

    counter = 0
    # print("\n\n\n\n\n\n\n HELLO \n\n\n\n\n\n\n\n")
    

    while True:
        
        picam2.capture_file(f"./{folderName}/timelapse_{counter}.jpg")  # Capture and save an image
        # print(f"Image saved as {counter}.jpg")
        app.logger.info(f"Image saved as {counter}.jpg")
        counter += 1
        
        time.sleep(5)


def background_task():
    """Function that runs in the background."""
    while True:
        # print("Background task is running...")
        app.logger.info("Background task is running...")
        time.sleep(5)  # Simulate work



def start_background_thread():
    """Start the background thread if it's not already running."""
    thread = threading.Thread(target=fuck, daemon=True)
    thread.start()

    thread2 = threading.Thread(target=display_stats, daemon=True)
    thread2.start()

    # thread5 = threading.Thread(target=fuck, daemon=True)
    # thread5.start()



# Start the background thread when the module is imported
start_background_thread()







if __name__ == '__main__':
    # Run background tasks to show current pi stats 
    # at the bottom of the terminal
    # bottom_text_thread = threading.Thread(target=display_stats, args=(picam2), daemon=True)
    # bottom_text_thread.start()

    # timelapse_thread = threading.Thread(target=fuck, args=(picam2), daemon=True)
    # timelapse_thread.start()

    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000, )

    


