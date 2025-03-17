This is a timelapse camera

Turn timelapse into a video.
Must be in directory to run command.
ffmpeg -framerate 10 -i "timelapse_%d.jpg" -c:v libx264 -pix_fmt yuv420p timelapse.mp4


Pi stats benchmarks

CPU Temp:
< 50
50-65
65-75
>75

CPU Usage
< 50
50-70
70-90
> 90

RAM Usage
< 60
60-75
75-90
>90

Disk Usage
< 70
70-80
80-95
95