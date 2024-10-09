 
'''x= range(1,11,1)
print(tuple(x))

output (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)'''


'''x = range(-1, -11, -1)
print(list(x))

output [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]'''

'''x = range(-4)
print(x)

output range(0, -4)'''

'''i  =int(input("enter even number"))
x= range(2,2*i+1,2)

print(list(x))

enter even number10
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
PS C:\Users\hp pc\OneDrive\Desktop\pyhton  P33\26 september range> python ./new.py
enter even number21
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]'''

# n= int(input("enter even number"))
# x= range(1,(2*n+1),2)
# print(list(x))

n = int(input("Enter an even number: "))
x = range(2, (2*n+1), 2)
print(list(x))
