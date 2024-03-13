from picamera import PiCamera
from time import sleep
class PhotoBooth:
    camera = PiCamera()
    shotnumber = 0
    location = None
    imageoverlay = None

    def __init__(self, location):
        self.location = location
        #self.camera.resolution = (1280, 720)

    def close(self):
        self.camera.stop_preview()
        sleep(.5)
        self.camera.close()

    def take_pic(self):
        imagelocation = self.location + "/image%s.png" % self.shotnumber
        for j in reversed(range(5)):
            self.camera.annotate_text = str(j + 1)
            self.camera.annotate_text_size = 160
            sleep(1)
        self.camera.annotate_text = ''

        #location = "/home/ian/Desktop/Photos/image%s.jpg" % self.shotnumber
        self.camera.capture(imagelocation)
        image = Image.open(imagelocation)
        self.shotnumber += 1
        return image

    def camerapreview(self):
        self.camera.start_preview()

    def imagepreview(self, img):
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))
        pad.paste(img, (0, 0))
        self.imageoverlay = self.camera.add_overlay(pad.tobytes(), size=img.size)
        self.imageoverlay.alpha = 255
        self.imageoverlay.layer = 3

    def imageremove(self):
        self.camera.remove_overlay(self.imageoverlay)
