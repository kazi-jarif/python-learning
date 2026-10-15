#strings are immutable. we need to duplicate to change
a="jarif is a good boy"
print(a.upper())
print(a.lower())
print(a.strip("boy"))
print(a.replace("boy","man"))
print(a.split())
print(a.center(50))
print(a.endswith("boy"))
print(a.count("boy"))
print(a.find("boy"))
print(a.islower())