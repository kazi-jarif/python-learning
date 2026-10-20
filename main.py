list=[1,33,4,5,"name",True]
print(type(list))
print(list)
print(list[0])
if 33 in list:
    print("yes")
else:
    print("no")
print(list[0:3])


#list comprehension
lst=[i for i in range(10) if i%2==0]
print(lst)

item=["rana","alif",'lima']
l_items=[l_items_list for l_items_list in item if "l" in l_items_list]
print(l_items)