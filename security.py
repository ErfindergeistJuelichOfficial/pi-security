from gpiozero import LED,Button
from time import sleep

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
        print("motion detected")
    else:
        red.off()


# https://gpiozero.readthedocs.io/en/latest/
