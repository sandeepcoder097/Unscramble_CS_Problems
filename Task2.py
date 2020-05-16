"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
record={}
t=0
for i,j,k,l in calls:
    if i not in record:
        record.update({i:l})
    if j not in record:
        record.update({j:l})
for k in record:
    for a,b,c,d in calls:
        if k==a or k==b:
            t=t+int(d)
    record[k]=t
    t=0
long_num=max(record,key=record.get)       
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(long_num,record[long_num]))
#worst case complexity=O(n^2)
