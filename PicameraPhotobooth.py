from gpiozero import Button
from PIL import Image

button = Button(17)
def main(camera):
    while True:
        input("Button Press")
        # button.wait_for_press()


if __name__ == '__main__':
    main(camera)

