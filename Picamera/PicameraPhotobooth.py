from PhotoBooth import PhotoBooth
from gpiozero import Button, LED
from time import sleep
from signal import pause

buttonphoto = Button(3)
buttoneffectforward = Button(26)
buttoneffectback = Button(1)
buttonexit = Button(2)
buttonlight = LED()

def main():
    pb = PhotoBooth()
    buttoneffectforward.when_pressed = pb.image_effects
    buttoneffectback.when_pressed = pb.image_effects(False)
    buttonexit.when_pressed = close(pb)

    try:
        pb.camera_preview()
        while not exit:
            buttonphoto.wait_for_press()
            for i in reversed(range(5)):
                pb.text(i)
                buttonlight.on()
                sleep(0.5)
                buttonlight.off()
                sleep(0.5)
            pb.text("CHEESE")
            sleep(0.5)
            pb.text()
            img = pb.take_pic()
            """
            pb.image_preview(img)
            sleep(3)
            pb.image_remove()
            """

    finally:
        pb.close()

def close(pb):
    if pb.camera.preview:
        pb.camera_preview_stop()
        print("stopped preview")
    else:
        print("closing camera")
        pb.close()

if __name__ == '__main__':
    main()

