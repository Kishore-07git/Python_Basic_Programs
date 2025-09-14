n=int(input("enter numbers:"))
temp=n
rev=0
while(n>0):
      dig=n%10
      rev=rev*10+dig
      n//=10
print(rev)