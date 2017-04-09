import csv
import pandas
import matplotlib.pyplot as py
from collections import Counter
a=[]
f = open("groceries.csv","rb")
reader = csv.reader(f)
for row in reader:
   a=a+row
f.close()

letter_counts = Counter(a)
df = pandas.DataFrame.from_dict(dict(letter_counts.most_common(5)), orient='index')
df.plot(kind='bar')
#py.show()

def recommend(pre,post,conf):
    print str(pre)+"=>"+str(post)