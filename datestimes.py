import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("THE TIME IN {} IS {}".format(country, local_time))
print("UTC IS {}".format(datetime.datetime.utcnow()))



