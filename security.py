from gpiozero import LED,Button
from time import sleep

red = LED(17)
button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
        red.on()
    else:
        print("Button is not pressed")
        red.off()


# https://gpiozero.readthedocs.io/en/latest/
