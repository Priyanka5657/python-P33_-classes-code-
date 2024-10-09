age = int(input("enter age:"))
if age<0:
    print("please enter valid age")
elif age>=0 and age<18:
    print("not eligible for vote")
elif age>=18 and age<60:
    print("you are adult")
elif age>=60:
    print("you are seniour citizon")

    