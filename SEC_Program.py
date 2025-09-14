#Swapping of tw numbers
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
a=a+b
b=a-b
a=a-b
print(a,b)

#Prime numbers using for loop
n=int(input("Enter a number: "))
c=0
for i in range(n-2):
    if n%i==0:
        c+=1
if(c==0):
    print("Prime number!")
else:
    print("Not a Prime Number!")

#Fibonacci series
n=int(input("enter a number"))
a=0
b=1
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c

#palindrome or not
n=int(input("Enter a value"))
b=str(n)
c=b[::-1]
print(c)
if(c==0):
    print("Palindrome!")
else:
    print("Not a Palindrome!")