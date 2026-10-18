#conditional operators: >,<,<=,>=,==,!=
a=int(input("enter your age : "))
if a<18:
    print("you are a teen")
    b=input("do you like chocolate ? (yes/no)")
    if b=="yes":
        print("then buy and eat")
    else:
        print("if you do , i will buy you one")
elif a==18:
    print("still teen")
    b=input("do you like chocolate ? (yes/no)")
    if b=="yes":
        print("then buy and eat")
    else:
        print("if you do , i will buy you one")
else:
    print("you are a man")
    b=input("do you like chocolate ? (yes/no)")
    if b=="yes":
        print("then buy and eat")
    else:
        print("if you do , i will buy you one")