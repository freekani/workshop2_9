import RPi.GPIO as GPIO
import time
BUZZER = 27
TONE_HIGH = 970
TONE_LOW = 770
RB = 21
RF = 20
LF = 23
LB = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RF, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LF, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LB, GPIO.OUT, initial=GPIO.LOW)


while True:
    com = input("前:1  後:2  終了:3")
    if com=="1":
        GPIO.output(RF,1)
        GPIO.output(LF,1)
        time.sleep(1.0)
        GPIO.output(RF,0)
        GPIO.output(LF,0)

    elif com=="2":
        GPIO.output(RB,1)
        GPIO.output(LB,1)
        time.sleep(1.0)
        GPIO.output(RB,0)
        GPIO.output(LB,0)
    
    elif com=="3":
        break

    elif com=="4":
        p = GPIO.PWM(BUZZER, TONE_HIGH)
        p.start(50)

    for i in range(5):
        p.ChangeFrequency(TONE_HIGH)
        time.sleep(0.65)
        p.ChangeFrequency(TONE_LOW)
        time.sleep(0.65)
    p.stop()

GPIO.cleanup()