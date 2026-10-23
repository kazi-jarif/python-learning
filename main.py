s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

s1.update(s2)
print(s1)

s1.intersection_update(s2)
print(s1)

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

s2.remove(6)
print(s2)

s2.clear()
print(s2)

del s1
print(s1)