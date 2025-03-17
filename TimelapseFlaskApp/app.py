from flask import Flask, Response
import logging
import sys
import time
import threading

# For the Pi stats
import psutil
import os
import time

from picamera2 import Picamera2

# Initialize camera
picam2 = Picamera2()  
picam2.start()

app = Flask(__name__)

import routes
from utils import fuck


def start_background_thread():
    """Start the background thread if it's not already running."""
    thread = threading.Thread(target=fuck, daemon=True)
    thread.start()


# start background threads
start_background_thread() 


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='0.0.0.0', port=5000, )
    

 


