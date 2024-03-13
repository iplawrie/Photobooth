from PhotoBooth import PhotoBooth
#from gpiozero import Button
from time import sleep

button = Button(17)
def main():
    location = "/home/ian/Desktop/Photos"
    pb = PhotoBooth(location)
    pb.camerapreview()
    input("Button Press")
    img = pb.take_pic()
    pb.imagepreview(img)
    sleep(3)
    pb.imageremove()
    sleep(5)
    pb.close()

if __name__ == '__main__':
    main()

