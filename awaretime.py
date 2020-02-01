import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))       # hora local
print("Naive UTC {}".format(utc_time))       # hora en el meridiano de greenwich

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_local_time.tzinfo))

gap_time = datetime.datetime(2020, 1, 31, 0, 0)
print(gap_time)
print(gap_time.timestamp())



