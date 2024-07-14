# from picamera2 import Picamera2, Preview
from time import sleep
from gpiozero import LED, Button
# import RPi.GPIO as GPIO

button = Button(0)

if button.is_pressed:
  print("Player 1 wins!")


# SHUTDOWN = 0
# LED = 24
# RESET = 16
# POWER = 20
# STATUSQ = 21

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)


# picam2 = Picamera2()
# picam2.start_preview(Preview.QTGL)
# picam2.start()
# sleep(5)
# picam2.close()