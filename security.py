import os
from gpiozero import LED,Button
from picamera2 import Picamera2, Preview
from time import sleep, strftime
from dotenv import load_dotenv
import ftplib

## setup env
load_dotenv()

FTP_USR = os.getenv('FTP_USR')
FTP_PWD = os.getenv('FTP_PWD')
FTP_URL = os.getenv('FTP_URL')

## setup GPIO
red = LED(12)
blue = LED(16)
green = LED(20)
yellow = LED(21)
button = Button(2)
motionSensor = Button(26)

## setup camera
picam2 = Picamera2()

## program loop
# TODO write functions
# TODO motion is alway on. off is a detection
# TODO save pic on USB
# TODO send pics only every 5 minutes (day mode)
# TODO time detector between 8pm an 8am send more pics (night mode)
# TODO add API to save events
# TODO delete pics on usb after x days. maybe an additional script than runs daily and check?
# TODO delete pics on ftp after x days. maybe an additional script than runs daily and check?
# TODO use current button to make a manuel pic
# TODO add shutdown button
# TODO red LED to show system is ready
# TODO blue LED to show motion detected
# TODO green LED to show pic on upload
# TODO yellow LED to show night/day mode)

def capture():
    time_str = strftime("%Y%m%d-%H%M%S")
    filename = "motion_" + time_str + ".jpg"

    picam2.start_and_capture_files(filename)
    green.on()
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_URL, 21)
        ftp.login(FTP_USR, FTP_PWD)
        file = open(filename,'rb')
        ftp.storbinary("STOR " + filename, file)
        file.close()
        ftp.quit()
    except Exception:
        print ("Failed FTP.")

    green.off()
    
while True:
    red.on()
    if button.is_pressed:
        capture()
    if motionSensor.when_released:
        blue.on()
        capture()
        blue.off()

# https://gpiozero.readthedocs.io/en/latest/


