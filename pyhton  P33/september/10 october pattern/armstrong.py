n=int(input("enter any number"))
m=x=n
sum=0
digit=0
i=0
while i<n:
    n=n//10
    digit=digit+1
while i<m:
    last_digit=m%10
    sum=sum+last_digit**digit
    m=m//10
if x==sum:
    print("it is armstrong number")
else:
    print("it is not armstrong number")