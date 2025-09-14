def fact_num(num):
    fact=1
    i=1
    while i<=num:
        fact*=i
        i+=1
        print(f"Factorial of {num} is : {fact}")
num=int(input("Enter a number to find Factorial :"))
fact_num(num)