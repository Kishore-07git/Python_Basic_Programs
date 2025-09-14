def factorial(fact):
    for i in range(1,fact):
        fact *= i
    print(f"Factorial of {fact} is:")
num=int(input("Enter a number: "))
factorial(num)