import csv
import random
from faker import Faker
from datetime import datetime


l=Faker('en_GB')
f=open("test.csv","r")
k=csv.reader(f)

g=open("test4.csv","a")
w=csv.writer(g)
w.writerow(('Firstname','Lastname','Email','Send Invite'))
for i in range(1000):

    w.writerow((l.name(),l.name(),l.email(),random.choice(['N'])))
f.close()
