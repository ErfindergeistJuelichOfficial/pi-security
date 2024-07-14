from gpiozero import LED,Button
from time import sleep
from picamera2 import Picamera2

picam2 = Picamera2()

red = LED(17)
button = Button(2)
motionSensor = Button(21)

while True:
    if button.is_pressed:
        red.on()
    else:
        red.off()
    if motionSensor.is_pressed:
        red.on()
        picam2.start_and_capture_file("Desktop/new_image.jpg")
        picam2.close()
    else:
        red.off()


# https://gpiozero.readthedocs.io/en/latest/
