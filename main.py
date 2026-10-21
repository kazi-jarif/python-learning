list=[11,2,4,5]
list.append(7)
list.sort()
list.reverse()
print(list)
print(list.index(2))
print(list.count(2))

m=list.copy()
m.append(10)
print(m)
m.insert(1,899)
print(m)

s=[4334,3434,343]
m.extend(s)
print(m)

k=m+list
print(k)