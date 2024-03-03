from time import sleep
from picamera import PiCamera

if __name__ == '__main__':
    with PiCamera(resolution = (1920, 1080), framerate = 30) as camera:
        camera.annotate_text_size = 30
        camera.start_preview()
        sleep(1)
        for i in range(1, 6):
            camera.annotate_text = i
            sleep(1)
        camera.stop_preview()
    print("exit")
    exit(0)
