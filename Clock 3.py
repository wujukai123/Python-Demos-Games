import time
import os

lcd={0:[' _  ','| | ','|_| '],\
     1:['    ','  | ','  | '],\
     2:[' _  ',' _| ','|_  '],\
     3:[' _  ',' _| ',' _| '],\
     4:['    ','|_| ','  | '],\
     5:[' _  ','|_  ',' _| '],\
     6:[' _  ','|_  ','|_| '],\
     7:[' _  ','  | ','  | '],\
     8:[' _  ','|_| ','|_| '],\
     9:[' _  ','|_| ',' _| ']}

def number2lcd(n):
    global lcd
    output = ['','','']
    l = len(str(n))
    while True:
        i = n // 10**(l-1)
        for j in range(3):
            output[j] += lcd[i][j]
        n = n % 10**(l-1)
        l -= 1
        if l == 0:
            break
    return output

def clock():
    t = time.localtime()
    hour = number2lcd(t.tm_hour)
    minute = number2lcd(t.tm_min)
    second = number2lcd(t.tm_sec)
    output = [hour[0]+' '+minute[0]+' '+second[0],hour[1]+'.'+minute[1]+'.'+second[1],hour[2]+'.'+minute[2]+'.'+second[2]]
    return output

while True:
    o = os.system('cls')
    for each in clock():
        print (each)
    time.sleep(1)
