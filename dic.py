import csv
f=open("student.csv","r")

r=csv.reader(f)
for row in r:
    print(row[0],row[2])

f.close()