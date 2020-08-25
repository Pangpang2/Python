from mako.template import Template

# t = Template("Hello ${name}")
# print t.render(name='yaya')
#
# t = Template(filename='/docs/tpl.txt', module_directory='/tmp/mako_modules')

# print t.render()

# -*- coding: UTF-8 -*-
print 'Hello World!'

from dateutil import tz
from dateutil.tz import tzlocal
from datetime import datetime
import time

# from_zone = tz.gettz('UTC')
# to_zone = tz.gettz('MST')
# start_date = datetime.strptime('2018-10-16 03:19:07', "%Y-%m-%d %H:%M:%S")
# print start_date
# start_date = start_date.replace(tzinfo=from_zone)
# print start_date
# start_date = start_date.astimezone(to_zone)
# print start_date
# print int(time.mktime(start_date.timetuple()))

# from datetime import datetime, timedelta, timezone
# print '---------------------------'

# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# cn_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print cn_dt

import pytz
from datetime import datetime


# print '-------------------------------'
# # usdate = datetime.strptime('2018-10-16 03:19:07', "%Y-%m-%d %H:%M:%S")
# usdate = datetime(2018, 10, 16, 3, 19, 7)
#
# central = pytz.timezone('UTC')
# local_us = central.localize(usdate)
# print local_us
#
#
# indiatime = local_us.astimezone(pytz.timezone('MST'))
# print(indiatime)
#
# print int(time.mktime(indiatime.timetuple()))
#
# print '-------------------------------'
#
# # get local time zone name
# print datetime.now(tzlocal()).tzname()
#
# # UTC Zone
# from_zone = tz.gettz('UTC')
# # China Zone
# to_zone = tz.gettz('MST')
#
# utc = datetime.utcnow()
# print (utc)
#
# # Tell the datetime object that it's in UTC time zone
# utc = utc.replace(tzinfo=to_zone)
# print (utc)
#
# # Convert time zone
# local = utc.astimezone(to_zone)
# print datetime.strftime(local, "%Y-%m-%d %H:%M:%S")

import dateutil
from datetime import timedelta
start_date = datetime.strptime('2018-10-16 03:19:07', "%Y-%m-%d %H:%M:%S")
start_date =  start_date.replace(tzinfo=tz.gettz('America/Los_Angeles'))
time_tuple =  start_date.timetuple()
print '        :' + str(int(time.mktime(time_tuple)))
print 'expected:' + '1539681547'
print 1539681547


# pst = pytz.timezone('America/Los_Angeles')
# t = datetime(year=2015, month=2, day=2)
# t = pst.localize(t)
# print time.mktime(t.timetuple())
# # outputs 1422864000.0
#
#
# utc = pytz.utc
# k = datetime(year=2015, month=2, day=2)
# k = utc.localize(k)
# print time.mktime(k.timetuple())
# # outputs 1422864000.0

# from datetime import datetime
# import pytz
# pacific = pytz.timezone('America/Los_Angeles')
# naive  = datetime(2015, 2, 2)
# pacific_dt = pacific.localize(naive, is_dst=None)
# print time.mktime(pacific_dt.timetuple())
#
# utc_dt = naive.replace(tzinfo=pytz.utc)
# print time.mktime(utc_dt.timetuple())
#
# print time.mktime(native) #NOTE: interpret as local time


