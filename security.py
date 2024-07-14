import os
from gpiozero import LED,Button
from picamera2 import Picamera2, Preview
from time import sleep, strftime
from dotenv import load_dotenv
import ftplib

load_dotenv()

FTP_USR = os.getenv('FTP_USR')
FTP_PWD = os.getenv('FTP_PWD')
FTP_URL = os.getenv('FTP_URL')

print("ftp host:")
print(FTP_URL)

picam2 = Picamera2()

red = LED(17)
button = Button(2)
motionSensor = Button(21)

while True:
    if button.is_pressed:
        red.on()
        timestr = strftime("%Y%m%d-%H%M%S")
        filename = "motion_" + timestr + ".jpg"
        picam2.start_and_capture_files(filename)

        session = ftplib.FTP(FTP_URL,FTP_USR,FTP_PWD)
        file = open(filename,'rb')
        session.storbinary('STOR picture', file)
        file.close()
        session.quit()

    else:
        red.off()
    if motionSensor.is_pressed:
        red.on()

    else:
        red.off()


# https://gpiozero.readthedocs.io/en/latest/

