This is a timelapse camera

Turn timelapse into a video.
Must be in directory to run command.
ffmpeg -framerate 10 -i "timelapse_%d.jpg" -c:v libx264 -pix_fmt yuv420p timelapse.mp4

