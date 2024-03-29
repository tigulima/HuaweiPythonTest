from datetime import datetime, timezone
import pandas
import os

# If you want to inspect another path, go ahead and change the "path" value
path = r'.'

name = os.listdir(path)
location = path
size = os.stat(path).st_size
last_mod = os.stat(path).st_mtime

year = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).year
month = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).month
day = datetime.fromtimestamp(os.stat(path).st_mtime, tz=timezone.utc).day

date = year, month, day

# "name" already contains the extension value.
pandas.DataFrame(data=[name, location, size, date], index=[0], columns=['name', 'location', 'size', 'date'])
print(name, location, size, date)
