"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique=set()
for i,j,k,l in calls:
    unique.add(i)
    unique.add(j)
for a,b,c in texts:
    unique.add(a)
    unique.add(b)
print("There are {} different telephone numbers in the records.".format(len(unique)))
#worst case complexity=O(n)