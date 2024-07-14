import os
from gpiozero import LED,Button
from picamera2 import Picamera2, Preview
from time import sleep, strftime
from dotenv import load_dotenv

load_dotenv()


FTP_USR = os.getenv('FTP_USR')
FTP_PWD = os.getenv('FTP_PWD')
FTP_URL = os.getenv('FTP_URL')



picam2 = Picamera2()

red = LED(17)
button = Button(2)
motionSensor = Button(21)

while True:
    if button.is_pressed:
        red.on()
        timestr = strftime("%Y%m%d-%H%M%S")
        picam2.start_and_capture_files("pic" + timestr + "_{:d}.jpg")
        # picam2.close()
        # picam2.start_and_capture_file("Desktop/new_image.jpg")
        # picam2.close()
    else:
        red.off()
    if motionSensor.is_pressed:
        red.on()

    else:
        red.off()


# https://gpiozero.readthedocs.io/en/latest/

