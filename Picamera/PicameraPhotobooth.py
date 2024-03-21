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
    #input("Button Press")
        #button.wait_for_press()
        #pb.text_countdown(5)
        #img = pb.take_pic()
    #pb.image_preview(img)
    #sleep(3)
    #pb.image_remove()
        #pb.text_countdown(5)
        #sleep(5)
        pause()
    finally:
        pb.close()

if __name__ == '__main__':
    main()

