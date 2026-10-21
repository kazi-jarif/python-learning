tup=(1,2,3,4,5)
l=list(tup)
l.append(6)
tup2=tuple(l)
print(type(tup2),tup2)

tup3=tup+tup2
print(tup3)
print(tup3.count(3))
print(tup3.index(3,4,-1))
print(len(tup3))