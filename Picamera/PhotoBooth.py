from picamera import PiCamera
from time import sleep
from PIL import Image
class PhotoBooth:
    camera = PiCamera()
    shotnumber = 0
    location = None
    imageoverlay = None

    def __init__(self, location = "/home/ian/Desktop/Photos"):
        self.location = location
        self.camera.annotate_text_size = 160
        #self.camera.resolution = (1280, 720)

    def close(self):
        self.camera_preview_stop()
        self.camera.close()

    def text(self, text):
        self.camera.annotate_text = text

    def clear_text(self):
        self.camera.annotate_text = ''

    def text_countdown(self, count):
        for i in reversed(range(count)):
            self.text(i + 1)
            sleep(1)
        self.text("Cheese")
        self.clear_text()

    def take_pic(self):
        imagelocation = self.location + "/image%s.png" % self.shotnumber
        #location = "/home/ian/Desktop/Photos/image%s.jpg" % self.shotnumber
        self.camera.capture(imagelocation)
        image = Image.open(imagelocation)
        self.shotnumber += 1
        return image

    def camera_preview(self):
        self.camera.start_preview()

    def camera_preview_stop(self):
        self.camera.stop_preview()

    def image_preview(self, img):
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))
        pad.paste(img, (0, 0))
        self.imageoverlay = self.camera.add_overlay(pad.tobytes(), size=img.size)
        self.imageoverlay.alpha = 255
        self.imageoverlay.layer = 3

    def image_remove(self):
        self.camera.remove_overlay(self.imageoverlay)
