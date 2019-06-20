import random
a = random.sample(range(1,30), 12)# .sample(range(frm _,_), lenght)
b = random.sample(range(1,30), 16)

unionList = []
unionList =set( [e for e in a  for i in b if e==i ])
print(unionList)