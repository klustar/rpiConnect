import datetime
import time
import csv

# 파일열기 및 최초열생성
nowDate=datetime.datetime.now()
title=nowDate.strftime('%Y-%m-%d')
f=open(title+'.csv','w',encoding='utf-8',newline='')
wr=csv.writer(f)
wr.writerow(['순번','시간','비고'])

for i in range(1,10):
    f=open(title+'.csv','a',encoding='utf-8',newline='')
    wr=csv.writer(f)
    nowDate=datetime.datetime.now()
    timelog=nowDate.strftime('%H:%M:%S')
    wr.writerow([i,timelog,' '])
    time.sleep(1)