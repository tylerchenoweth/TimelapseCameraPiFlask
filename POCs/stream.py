from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)  # Open a preview window
picam2.start()
time.sleep(15)  # Keep the preview open for 5 seconds
picam2.stop_preview()
