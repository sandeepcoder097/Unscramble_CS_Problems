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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

tele=set()
nontele=set()
for i,j,k,l in calls:
    tele.add(i);
    nontele.add(j)
for a,b,c in texts:
    nontele.add(a);
    nontele.add(b);
possible_telemarketers=tele-nontele
print("These numbers could be telemarketers: ")
for a in sorted(possible_telemarketers):
    print(a)
#complexity O(nlogn)