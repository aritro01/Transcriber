import subprocess

def slice():
    command = 'ffmpeg -i audio.wav -f segment -segment_time 30 -c copy parts/out%09d.wav'
    subprocess.call(command, shell=True)
