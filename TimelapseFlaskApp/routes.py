from utils import *

from app import app
from flask import Response, stream_with_context
import datetime

# For the camera streaming
import cv2
# from picamera2 import Picamera2

from app import picam2  # import the initialized Picamera2 instance

from flask import render_template



# NOT in use 
# @app.route('/log')
# def log_message():
#     app.logger.info("Log route accessed")
#     return "Logged a message!"




@app.route('/')
def dasboard(): 
    return render_template('dashboard.html', context = get_display_stats())


@app.route('/stream')
def stream():
    app.logger.info("Stream route accessed")
    return Response(generate_frames(),  mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stats')
def stats():
    # context = get_display_stats['cpu_usage']
    return Response(stream_with_context(get_display_stats()), mimetype='text/event-stream')

















# def generate_frames():
#     while True:
#         frame = picam2.capture_array()
#         _, buffer = cv2.imencode(".jpg", frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('htmlpage.html')

# @app.route('/stream')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')




