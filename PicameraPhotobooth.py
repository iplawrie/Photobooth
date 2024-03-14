from PhotoBooth import PhotoBooth
#from gpiozero import Button, LED
from time import sleep

#button = Button(17)
#exitbutton = Button()
#buttonlight = LED()

def main():
    location = "/home/ian/Desktop/Photos"
    pb = PhotoBooth(location)
    pb.camera_preview()
    input("Button Press")
    pb.text_countdown(5)
    img = pb.take_pic()
    pb.image_preview(img)
    sleep(3)
    pb.image_remove()
    sleep(5)
    pb.close()

if __name__ == '__main__':
    main()

