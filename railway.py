import requests
from bs4 import BeautifulSoup
# import html5lib
import time


url = 'https://www.railway.gov.tw/tra-tip-web/tip'
# 存車站名車＆代碼
staDic = {}
# 取得時間
today = time.strftime('%Y/%m/%d')

sTime = '06:00'
eTime = '12:00'

def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('URL發生錯誤'+url)
        return