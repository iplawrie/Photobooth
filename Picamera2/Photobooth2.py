from picamera2 import Picamera2, Preview
from time import sleep, strftime
from PIL import Image

class PhotoBooth:
    camera = Picamera2()
    shotnumber = 0
    location = None
    imageoverlay = None

    def __init__(self, location = "/home/ian/Desktop/Photos", size = (800, 600)):
        self.location = location
        config = self.camera.create_preview_configuration({"size" : size})
        self.camera.configure(config)

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
        image = Image.open(imagelocation)
        self.camera.capture(imagelocation)
        self.shotnumber += 1
        return image

    def camera_preview(self):
        self.camera.start_preview(Preview.QTGL)
        self.camera.start()

    def camera_preview_stop(self):
        self.camera.stop_preview()

    def image_preview(self, img):
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))
        pad.paste(img, (0, 0))
        self.camera.set_overlay(pad.tobytes())

    def image_remove(self):
        pass