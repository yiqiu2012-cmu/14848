import sys

current_date = None
current_max = -9999
date = None

for line in sys.stdin:
    line = line.strip()
    date, temp = line.split('\t', 1)
    try:
        temp = int(temp)
    except ValueError:
        continue
    if current_date == date:
        current_max = max(current_max, temp)
    else:
        if current_date:
            print ('%s\t%s' % (current_date, current_max)) 
        current_max = temp
        current_date = date
if current_date == date:
    print ('%s\t%s' % (current_date, current_max))