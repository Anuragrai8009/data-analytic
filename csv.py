import csv
f = open ("varsha.csv",'a',newline='')

wo =csv.writer(f)
data = [["a","b","c","d"],[16,14,12,10],[26,24,22,20],[36,34,32,20]]
wo.writerows(data)
f.close()


print("<--------------------------------------------------->")


import csv
f = open("rahul.csv",'r')
re = csv.reader(f)
li  =list(re)
for row in li:
    print(row)