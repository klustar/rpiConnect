import RPI.GPIO as GPIO
import time
import csv

GPIO.setmode(GPIO.BCM)
trig=13
echo=19
f=open('data.csv','w',encoding='utf-8',newline='')
wr=csv.writer(f)

print("start")

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

try:
    while True:
        GPIO.output(trig,False)
        time.sleep(0.5)

        GPIO.output(trig,True)
        time.sleep(0.00001)
        GPIO.output(trig,False)

        while GPIO.input(echo)==0:
            pulse_start=time.time()

        while GPIO.input(echo)==1:
            pulse_end=time.time()

        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17000
        distance=round(distance,2)

        print("Distance :",distance,"cm")

        f=open('data.csv','a',newline='')
        wr=csv.writer(f)

except:
    f.close()
    GPIO.cleanup()