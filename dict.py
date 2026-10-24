dic={
    123:"jarif",
    545:"rana",
    766:"ratul"
}

print(dic)

#if i want error whenever system can't find value through the key
# print(dic[1243])
#if i don't want error whenever system can't find value through the key
print(dic.get(1243))

print(dic.keys())

for key in dic.keys():
    print(f"the name of id {key} is {dic[key]}")


print(dic.items())

for key,value in dic.items():
    print(f"the name of id {key} in {value}")