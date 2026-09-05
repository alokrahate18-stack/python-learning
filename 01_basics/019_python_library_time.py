import time
from datetime import datetime

now = datetime.now()
print("Original time:")
print(now)

print("\nHours:Minutes:Seconds")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

print("\nHours:")
timestamp = time.strftime('%H')
print(timestamp)

print("\nMinutes:")
timestamp = time.strftime('%M')
print(timestamp)

print("\nSeconds:")
timestamp = time.strftime('%S')
print(timestamp)

print("\nMicroseconds:")
timestamp = datetime.now().strftime('%f') # Note: Do not use time.strptime('%f'). Instead, use datetime.now().strftime('%f')

print(timestamp)

print("\nWeekday Name (Abbreviated):")
timestamp = time.strftime('%a')
print(timestamp)

print("\nWeekday Name (Full):")
timestamp = time.strftime('%A')
print(timestamp)

print("\nMonth Name (Abbreviated):")
timestamp = time.strftime('%b')
print(timestamp)

print("\nMonth Name (Full):")
timestamp = time.strftime('%B')
print(timestamp)

print("\nDate and Time:")
timestamp = time.strftime('%c')
print(timestamp)

print("\nDay of the Month:")
timestamp = time.strftime('%d')
print(timestamp)

print("\nHour (24-hour clock):")
timestamp = time.strftime('%H')
print(timestamp)

print("\nHour (12-hour clock):")
timestamp = time.strftime('%I')
print(timestamp)

print("\nDay of the Year:")
timestamp = time.strftime('%j')
print(timestamp)

print("\nMonth of the Year:")
timestamp = time.strftime('%m')
print(timestamp)

print("\nEquivalent of AM or PM:")
timestamp = time.strftime('%p')
print(timestamp)

print("\nWeek of the Year (Sunday as the first day of the week):")
timestamp = time.strftime('%U')
print(timestamp)

print("\nDay of the Week (Monday is 1; Sunday is 7):")
timestamp = time.strftime('%u')
print(timestamp)

print("\nWeekday [0(Sunday), 6(Saturday)]:")
timestamp = time.strftime('%w')
print(timestamp)

print("\nWeek of the Year (Monday as the first day of the week):")
timestamp = time.strftime('%W')
print(timestamp)

print("\nDate:")
timestamp = time.strftime('%x')
print(timestamp)

print("\nTime:")
timestamp = time.strftime('%X')
print(timestamp)

print("\nYear (Without Century):")
timestamp = time.strftime('%y')
print(timestamp)

print("\nYear (With Century):")
timestamp = time.strftime('%Y')
print(timestamp)

print("\nTime Zone Offset (+HHMM or -HHMM):")
timestamp = time.strftime('%z')
print(timestamp)

print("\nTime Zone Name:")
timestamp = time.strftime('%Z')
print(timestamp)

print("\nISO Year:")
timestamp = time.strftime('%G')
print(timestamp)

print("\nISO Week:")
timestamp = time.strftime('%V')
print(timestamp)

print("\n% Character:")
timestamp = time.strftime('%%')
print(timestamp)

print("\nGive time as input (String → Time): ")
date = time.strptime("06-09-2026", "%d-%m-%Y")
print(date)


        # strptime()   📖 READ
        #              String → Time

        # strftime()   ✍️ WRITE
        #              Time → String
