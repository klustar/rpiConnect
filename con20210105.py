import RPI.GPIO as GPIO
import datetime
import time
import csv

# 파일열기 및 최초열생성
nowDate=datetime.datetime.now()
title=nowDate.strftime('%Y-%m-%d')
f=open(title+'.csv','w',encoding='utf-8',newline='')
wr=csv.writer(f)
wr.writerow(['순번','시간','비고'])

# 변수설정
trig=13
echo=19
doorWidth=60
i=1

# GPIO핀 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

# 사전준비종료 알림문구
print("service start")

try:
    while True:
        if sonic(trig,echo)<doorWidth:
            f=open(title+'.csv','a',encoding='utf-8',newline='')
            wr=csv.writer(f)
            nowDate=datetime.datetime.now()
            timelog=nowDate.strftime('%H:%M:%S')
            wr.writerow([i,timelog,' '])

except:
    f.close()
    GPIO.cleanup()

def sonic(oPin,iPin):
    """
        초음파센서의 거리를 측정하는 코드를 함수로 정의
        oPin : 초음파센서의 trig핀
        iPin : 초음파센서의 echo핀
    """
    GPIO.output(oPin,False)
    time.sleep(0.5)

    GPIO.output(oPin,True)
    time.sleep(0.00001)
    GPIO.output(oPin,False)

    while GPIO.input(iPin)==0:
        pulse_start=time.time()

    while GPIO.input(iPin)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17000
    distance=round(distance,2)

    return distance