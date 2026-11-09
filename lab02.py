d1=float(input())
v1=float(input())
t=float(input())
d2=float(input())
v2=float(input())
t1= (d1 / v1)/24
t2= (d2 / v2)/24
t3= t1 - t
if t3<t2:
    print('True')
else:
    print('False')

