"""
    - 날짜가 바뀌면 해당 날짜와 동일한 이름의 csv파일을 생성 (년도월일)
    - 테스트용 : 매시간마다 정상 작동 테스트용으로 열생성 (시분초)
"""
import datetime
import time
import csv

setDate=datetime.datetime.now()
setDate=setDate.strftime('%Y%m%d')
setTime=setDate.strftime('%H')
i=1

while True:
    nowDate=datetime.datetime.now()
    title=nowDate.strftime('%Y-%m-%d')
    nowDate=nowDate.strftime('%Y%m%d')
    nowTime=nowDate.strftime('%H')

    if nowDate!=setDate:
        # 파일열기 및 최초열생성
        f=open(title+'.csv','w',encoding='utf-8',newline='')
        wr=csv.writer(f)
        wr.writerow(['순번','시간','비고'])
        f.close()
    else:
        # 테스트 시간 출력
        if nowTime!=setTime:
            f=open(title+'.csv','a',encoding='utf-8',newline='')
            wr=csv.writer(f)
            nowDate=datetime.datetime.now()
            timelog=nowDate.strftime('%H:%M:%S')
            wr.writerow([i,timelog,' '])
            i=i+1
            f.close()
        
    setDate=datetime.datetime.now()
    setDate=setDate.strftime('%Y%m%d')
    setTime=setDate.strftime('%H')