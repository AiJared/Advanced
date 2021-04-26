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