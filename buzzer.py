import RPi.GPIO as GPIO
import time

BUZZER = 27
TONE_HIGH = 970
TONE_LOW = 770

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(BUZZER, TONE_HIGH)
p.start(50)

for i in range(5):
        p.ChangeFrequency(TONE_HIGH)
        time.sleep(0.65)

        p.ChangeFrequency(TONE_LOW)
        time.sleep(0.65)
p.stop()

GPIO.cleanup()