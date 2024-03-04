from time import sleep
from picamera2 import Picamera2, Preview

if __name__ == '__main__':
    with Picamera2() as camera:
        camera_config = camera.create_preview_configuration()
        camera.configure(camera_config)
        camera.start_preview()
        camera.start()
        sleep(5)
        
    print("exit")
    exit(0)
