t1 = (1,2,3)
t2 = (4,5,6)
t3 = []


i = 0
while i < len(t1):
    t3.append(t1[i])
    i+=1

i = 0
while i < len(t2):
    t3.append(t2[i])
    i+=1

t3 = tuple(t3)
print(t3)



