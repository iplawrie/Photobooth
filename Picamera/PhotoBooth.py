from picamera import PiCamera
from time import sleep, strftime
from PIL import Image
import numpy as np

class PhotoBooth:
    camera = None
    shotnumber = 0
    location = None
    imageoverlay = None
    background = None
    previewesolution = None
    effectnum = 0
    effects = ['none', 'negative', 'solarize',
               'sketch', 'denoise', 'emboss',
               'oilpaint', 'hatch', 'gpen',
               'pastel', 'watercolor', 'film',
               'blur', 'saturation', 'colorswap',
               'washedout', 'posterise', 'colorpoint',
               'colorbalance', 'cartoon',
               'deinterlace1', 'deinterlace2']


    def __init__(self, location = "/home/ian/Desktop/Photos", previewresolution = (1640, 1282), camresolution = (3280, 2464)):
        self.camera = PiCamera()
        self.camera.resolution = camresolution
        self.previewresolution = previewresolution
        self.location = location
        self.camera.annotate_text_size = 160

    def close(self):
        self.camera.close()

    def text(self, text = ''):
        self.camera.annotate_text = str(text)

    def text_countdown(self, count):
        for i in reversed(range(count)):
            self.text(i + 1)
            sleep(1)
        self.text("Cheese!")
        sleep(1)
        self.clear_text()

    def image_effects(self, forward = True):
        if forward:
            self.effectnum += 1
        else:
            self.effectnum -= 1

        if self.effectnum < 1:
            self.effectnum = 21
        elif self.effectnum > 21:
            self.effectnum = 0

        effect = self.effects[self.effectnum]
        self.camera.image_effect = effect
        self.text(effect)

    def take_pic(self):
        imagelocation = self.location + "/image%s_%s.png" % (self.shotnumber, strftime("%Y.%m.%d-%H:%M:%S"))
        self.camera.capture(imagelocation, use_video_port=False, format='png')
        image = Image.open(imagelocation)
        self.shotnumber += 1
        return image

    def camera_preview(self):
        self.camera.framerate = 40
        a = np.zeros((720, 1280, 3), dtype=np.uint8)
        a[720:1280:] = 0
        self.camera.start_preview(resolution = self.previewresolution)
        self.background = self.camera.add_overlay(a.tobytes(),size=(1280, 720), format='rgb')

    def camera_preview_stop(self):
        self.camera.remove_overlay(self.background)
        self.camera.stop_preview()

    def image_preview(self, img):
        pad = Image.new('RGB', (
            ((img.size[0] + 31) // 32) * 32,
            ((img.size[1] + 15) // 16) * 16,
        ))
        pad.paste(img, (0, 0))
        self.imageoverlay = self.camera.add_overlay(pad.tobytes(), size=img.size, alpha = 255, layer = 3)

    def image_remove(self):
        self.camera.remove_overlay(self.imageoverlay)
