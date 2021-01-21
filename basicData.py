"""
    - 날짜가 바뀌면 해당 날짜와 동일한 이름의 csv파일을 생성 (년도월일)
    - 테스트용 : 매시간마다 정상 작동 테스트용으로 열생성 (시분초)
"""
import datetime
import time
import csv

setDate=datetime.datetime.now()
setDate=setDate.strftime('%Y%m%d')

try:
    while True:
        nowDate=datetime.datetime.now()
        title=nowDate.strftime('%Y-%m-%d')

        if nowDate.strtime('%Y%m%d')!=setDate.strtime('%Y%m%d'):
            # 파일열기 및 최초열생성
            f=open(title+'.csv','w',encoding='utf-8',newline='')
            wr=csv.writer(f)
            wr.writerow(['순번','시간','비고'])
        else:
            # 센서 측정부분
            if sonic(trig,echo)<doorWidth:
                f=open(title+'.csv','a',encoding='utf-8',newline='')
                wr=csv.writer(f)
                nowDate=datetime.datetime.now()
                timelog=nowDate.strftime('%H:%M:%S')
                wr.writerow([i,timelog,' '])
                i=i+1
        
        setDate=datetime.datetime.now()
except:
    f.close()