from PhotoBooth import PhotoBooth
from gpiozero import Button, LED
from time import sleep
from signal import pause

Button.was_held = False
button = Button(26)
#exitbutton = Button()
#buttonlight = LED()

def main():
    pb = PhotoBooth()
    button.when_pressed = pb.image_effects()

    try:
        pb.camera_preview()
        pause()
    finally:
        pb.close()

if __name__ == '__main__':
    main()

