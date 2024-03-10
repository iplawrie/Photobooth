import sys
from time import sleep, strftime
from picamera2 import Picamera2, Preview

if __name__ == '__main__':
    with Picamera2() as camera:
        camera_config = camera.create_preview_configuration()
        camera.configure(camera_config)
        camera.start_preview(Preview.QTGL)
        camera.start()
        sleep(5)
        metadata = camera.capture_file("/home/ian/Desktop/Photos/image%s.png" % strftime("%Y%m%d-%H%M%S"))
        print(metadata)
        camera.close()
    print("exit")
    exit(0)
