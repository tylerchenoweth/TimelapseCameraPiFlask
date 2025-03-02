from picamera2 import Picamera2
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

picam2.start()
print("Recording video...")
picam2.start_and_record_video("video.h264", duration=10)  # Record 10s
print("Video saved as video.h264")
