#coding:utf-8
import RPi.GPIO as GPIO
import time
BUZZER = 18
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
        com = input("front:1  back:2  end:3  buzzer:4")
        if com==1:
                GPIO.output(RF,1)
                GPIO.output(LF,1)
                time.sleep(1.0)
                #GPIO.output(RF,0)
                #GPIO.output(LF,0)

        elif com==2:
                GPIO.output(RB,1)
                GPIO.output(LB,1)
                time.sleep(1.0)
                #GPIO.output(RB,0)
                #GPIO.output(LB,0)

        elif com==3:
                break

        elif com==4:
                p = GPIO.PWM(BUZZER, 1)
                p.start(50)
                p.ChangeFrequency(970)
                time.sleep(0.65)
                p.ChangeFrequency(770)
                time.sleep(0.65)
                p.ChangeFrequency(970)
                time.sleep(0.65)
                p.ChangeFrequency(770)
                time.sleep(0.65)
                p.ChangeFrequency(970)
                time.sleep(0.65)
                p.ChangeFrequency(770)
                time.sleep(0.65)
                p.ChangeFrequency(970)
                time.sleep(0.65)
                p.ChangeFrequency(770)
                time.sleep(0.65)
                p.stop()

GPIO.cleanup()
