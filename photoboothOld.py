import time
from picamera import PiCamera
from gpiozero import Button
from time import sleep
from PIL import Image

button = Button(17)
i = 0
IMG_NAME = "image.jpg"

img = Image.open('pi_layover4.png')

def take_pic():
    global i
    camera.capture(IMG_NAME)
    #camera.capture("/home/pi/image%s.jpg" % i)
    i += 1

camera = PiCamera()
camera.start_preview()
pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
# Paste the original image into the padded one
pad.paste(img, (0, 0))

o = camera.add_overlay(pad.tostring(), size=img.size)

o.alpha = 255
o.layer = 3
button.wait_for_press()
for j in reversed(range(3)):
    camera.annotate_text = str(j+1)
    camera.annotate_text_size=160
    sleep(1)
camera.annotate_text = ''
take_pic()
camera.stop_preview()


# your twitter app keys goes here
consumer_key = 'hhhh' # put twitter API Key here
consumer_secret = 'hhhh' # put twitter API Secret here
access_token = 'hhh-hhh' # twitter access token here
access_token_secret = 'hhhh' # twitter access token secret

from twython import Twython
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

time_now = time.strftime("%H:%M:%S") # get current time
date_now =  time.strftime("%d/%m/%Y") # get current date
tweet_txt = "Photo captured by @ PiPicsUSA at " + time_now + " on " + date_now

message = tweet_txt
with open(IMG_NAME, 'rb') as photo:
    twitter.update_status_with_media(status=message, media=photo)

print ("Posting tweet with picture...\n")