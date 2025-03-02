from app import app
from flask import Response
import datetime

# For the camera streaming
import cv2
from picamera2 import Picamera2

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    app.logger.info(datetime.datetime.now())

    return str(datetime.datetime.now())


@app.route('/log')
def log_message():
    app.logger.info("Log route accessed")
    return "Logged a message!"


# For streaming
picam2 = Picamera2()
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode(".jpg", frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/stream')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
