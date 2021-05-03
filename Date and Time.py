#  Parsing a string into a timezone aware datetime object
import datetime
dt = datetime.datetime.strptime("2021-04-26T9:09:40-0500", "%Y-%Mn-%dT%H:%M:%S%z")
# Constructing timezone-aware datetimes
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))

dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
print(dt.tzname())

dt = datetime(2021, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
print(dt.tzname())

#  Zones with daylight savings time
from datetime import datetime
from dateutil import tz
local = tz.gettz() #  local time
PT = tz.gettz('US/Pacific')  #  Pacific time

dt_l = datetime(2021, 1, 1, 12, tzinfo=local) # Iam in EST
dt_pst = datetime(2021, 1, 1, 12, tzinfo=PT)
dt_pdt = datetime(2021, 7, 1, 12, tzinfo=PT) #  DST is handled automatically
print(dt_l)
print(dt_pst)
print(dt_pdt)
#  Computing Time Differences
from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
delta = now - then
print(delta.days)
print(delta.seconds)
#  n days after date
def get_n_days_after_date(date_format = "%d %B %Y", add_days = 120):

    date_n_days_after = datetime.datetime.now() + timedelta(days = add_days)
    return date_n_days_after.strftime(date_format)
# n days before date
def get_n_days_before_date(date_format = "%d %B %Y", add_days = 120):

    date_n_days_before = datetime.datetime.now() + timedelta(days = add_days)
    return date_n_days_before.strftime(date_format)

#  Basic Datetime Usage
# Date Object
import datetime
today = datetime.date.today()
new_year = datetime.date(2021, 1, 1)

# Time Object
noon = datetime.time(12, 0, 0)

# Current datetime
now = datetime.datetime.now()

# Datetime Object
millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)

# Subtracrion of noon from today
print('Time since the millenium at midnight:',
      datetime.datetime(today.year, today.month, today.day) - millenium_turn)
print('Since the millenium at noon:',
      datetime.datetime.comine(today, noon) - millenium_turn)

# Switching Between timezones
from datetime import datetime
from dateutil import tz

utc = tz.tzutc()
local = tz.tzlocal()

utc_now = utc_now.replace(tzinfo=utc)
utc_now #  Timezone-ware

local_now = utc_now.astimezome(local)
local_now #  Converted to lacal time

#  Simple Date Arithmetic
import datetime
today = datetime.date.today()
print('Today:', today)
yesterday  = today - datetime.timedelta(days=1)
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)

#  Converting Timestamp to datetime
import time
from datetime import datetime
seconds_since_epoch=time.time()

utc_date=datetime.utcfromtimestamp(seconds_since_epoch)

# Separating months from a date accurately
import calendar
from datetime import date

def mothdelta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta -1) // 12
    if not m: m = 12
    d = min(date.day, calendar.monthrange(y, m) [1])
    return date.replace(day=d, month=m, year=y)

next_month = monthdelta(date.today(), 1)

# Using dateutils module

import datetime
import dateutil.relativedelta
d = datetime.datetime.strptime("2013-03-31", "%Y-%m-%d")
d2 = dateutil.relativedelta.relativedelta(months=1)

# Parsing an arbitrary ISO 8601 timestamp with minimal libraries

str(datetime.datetime(2016, 7, 22, 25, 59, 555555))
# but if fraction is 0 not fractional part is output
str(datetime.datetime(2016, 7, 22, 9, 25, 55, 0))

import iso8601
iso8601.parse_date('2016-07-22 09:25:59')
iso8601.parse_date('2016-07-22 09:25:59+03:00')
iso8601.parse_date('2016-07-22 09:25:59Z')
iso8601.parse_date('2016-07-22T09:25:59.000111+03:00')

iso8601.parse_date('2016-07-22 09:25:59', default_timezone=None)
iso8601.parse_date('2016-07-22 09:25:59Z', default_timezone=None)

#  Get an ISO 8601 Timestamp
#  Without timezone, with microseconds
from datetime import datetime

datetime.now().isoformat()

#  With timezone, with microsecnds
from datetime import datetime
from dateutil.tz import tzlocal

datetime.now(tzlocal()).isoformat()

#  With timezone, without microseconds
from datetime import datetime
from dateutil.tz import tzlocal

datetime.now(tzlocal()).replace(microsecnds=0).isoformat()

# Parsing a string with a shirt timezone name into a timezone aware datetime object
from dateutil import tz
from dateutil.parser import parse

ET = tz.gettz('US/Eastern')
CT = tz.gettz('US/Central')
MT = tz.gettz('US/Mountain')
PT = tz.gettz('US/Pacific')

us_tzinfos = {'CST': CT, 'CDT': CT,
             'EST': ET, 'EDT': ET,
             'MST': MT, 'MDT': MT,
             'PST': PT, 'PDT': PT}

dt_est = parse('2014-01-02 04:00:00 EST', tzinfos=us_tzinfos)
dt_pst = parse('2016-03-11 16:00:00 PST', tzinfos=us_tzinfos)
dt_est
dt_pst

dt_fixed = dt.tzinfo.localize(dt.replace(tzinfo=None))
dt_fixed.tzinfo

# Fuzzy datetime parsing(extracting datetime out of a text)
from dateutil.parser import parse

dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)
print(dt)

# Iterate over dates
import datetime
# The size of each steps in days
day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7*day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)