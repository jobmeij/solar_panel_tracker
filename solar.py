from suncalc import get_position, get_times
import pandas as pd
import numpy as np
import time
from datetime import datetime, timezone

# Usefull sources:
# Suncalc documentation:
# https://pypi.org/project/suncalc/
# 
# computed angles: azimuth and altitude:
# https://www.timeanddate.com/astronomy/horizontal-coordinate-system.html
#
#

################# TODOs
# 1. import weather info to detect storm
# 2. compute angle for panels
# 3. set angle to correct place/file 

# Update interval 
Tsample = 1;                # Seconds between updating position 

# Set coordinates of location (Wageningen)
lat = float(51.97)         # North
lon = float(5.67)          # East

# Get current date
date = datetime.now(timezone.utc)
print('Current time (UTC):')
print(date)
print('\n')

# Get position of sun at set location
pos = get_position(date, lon, lat)
print('Current position:')
print(pos)
print('\n')

# Get times
times = get_times(date, lon, lat)
print('Current times:')
print(times)
print('\n')

print(len(times))

print('Sunrise is at:')
print(times['sunrise'])
print('Sunset is at:')
print(times['sunset'])



temp = times['sunrise'] == date
print(temp)

#temp = date < times['sunrise']
#print(temp)

# Check if current time is between sunrise and sunset 
# TODO 

i = 0;
while 1:
    #print(i)
    #i = i+1;
    
    current_solar_pos = pos = get_position(datetime.now(timezone.utc), lon, lat)
    print(current_solar_pos)

    # TODO convert sun position to panel angle. 
    
    time.sleep(1);

    








