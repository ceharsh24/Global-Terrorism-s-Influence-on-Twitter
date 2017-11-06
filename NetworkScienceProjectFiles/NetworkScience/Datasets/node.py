import csv
from collections import Counter
from itertools import imap
from operator import itemgetter
f_date = open('node.csv', 'w')
f_date.write("Id, Label" + "\n")

with open('tweets.csv') as f:
    next(f) # skip the header
    cn = Counter(imap(itemgetter(1), csv.reader(f)))
    count = 0
    for t in cn.iteritems():
        print("{} ------------->>>> {} ".format(*t))
        f_date.write(str(count)+ "," + ("{}").format(*t)+ "\n")
        count = count + 1
