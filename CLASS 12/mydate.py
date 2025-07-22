#import all
#from datetime import *

#import by choice
from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)

today = date.today()
print(today)

formatted = now.strftime("%d-%m-%Y %H:%M")
print(formatted)

tomorrow = today + timedelta(days=45)
print(tomorrow)

one_hour_ago = now - timedelta(hours=1)
print(one_hour_ago)