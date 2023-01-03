from datetime import datetime

tdate = datetime.today()
today = tdate.strftime("%d-%m-%Y")

ntime = datetime.now()
now = ntime.strftime("%I:%M %p")
print(today)
print(now)