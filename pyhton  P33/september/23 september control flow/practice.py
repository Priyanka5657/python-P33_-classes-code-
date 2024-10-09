# x = input ("even no") 
# if(x>=)
# print (x)
# print(type(x))  


# x=int (input("s:"))
# if (x>=17):
#     print("eligible to vote",end='.') 
# else:
#     print("you are not eligible to vote")
#     print("thanks for visit")
# <-----------without using third variable----------------->
# x=10
# y=20
# print(x)
# print(y)
# print(f'value of x is{x} and value of y is {y}')  # print karne ka f string syntax

# <-----------by  using third variable-----------------
# int
# x=10
# y=20
# x = x+y =30
# y = x-y =10
# x = x-y =20
# print(f'value of x is{x} and value of y is {y}')  # print karne ka f string syntax

def is_even(n):
    return n / 2 == int(n / 2)

num = int(input("Enter a number: "))
if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")


