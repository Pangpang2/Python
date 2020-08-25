#coding=utf-8
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
import string


index = "https://www.12306.cn/index/index.html"
left_ticket = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={fs}&ts={ts}&date={date}&flag={is_student},{is_high},Y"

beijing = '北京,BJP'
shuyang = '沭阳,FMH'
on_date = '2019-01-30'
is_student = 'N'
is_high = 'N'

def get_left_ticket_url(fs, ts, on_date, is_student='N', is_high='N'):
    url = left_ticket.format(fs=beijing, ts=shuyang, date=on_date, is_student=is_student, is_high=is_high)
    return quote(url, safe=string.printable)

url = get_left_ticket_url(beijing, shuyang,on_date)
response = request.urlopen(url)
html = response.read()

bs = BeautifulSoup(html, 'html.parser')
print(bs.prettify())





