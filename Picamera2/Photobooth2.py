from picamera2 import Picamera2
from time import sleep, strftime

class PhotoBooth:
    camera = Picamera2()
    shotnumber = 0
    location = None
    imageoverlay = None

    def __init__(self, location = "/home/ian/Desktop/Photos"):
        self.location = location
        self.camera.configure(self.camera.create_preview_configuration())

    def close(self):
        self.camera_preview_stop()
        self.camera.close()

    def text(self, text):
        pass

    def clear_text(self):
        pass

    def text_countdown(self, count):
        for i in reversed(range(count)):
            pass

    def take_pic(self):
        imagelocation = self.location + "/image%s_%s" % (self.shotnumber, strftime("%Y%m%d-%H%M%S"))
        self.shotnumber += 1

    def camera_preview(self):
        pass

    def camera_preview_stop(self):
        self.camera.stop_preview()

    def image_preview(self):
        pass

    def image_remove(self):
        pass