import sys

for line in sys.stdin:
    line = line.strip()
    #filter out invalid record
    q_list = ['0', '1', '4', '5', '9']
    bytearr = line.encode()
    temp = bytearr[87:92].decode()
    quality = bytearr[92:93].decode()
    yearMonthDay = bytearr[15:23].decode()
    if (temp == '+9999' or quality not in q_list):
        continue
    # map yearMonthDay to temp
    print ('%s\t%s' % (yearMonthDay, temp))
    

