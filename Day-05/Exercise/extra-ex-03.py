def factorial(n):
    if n<0:
        return "Invalid input! Factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        result =1
        for i in range(2,n+1):
            result *=i
        return result

n = int(input("Enter a number: \n"))
print(f"Factorial of {n} is {factorial(n)}")

#  This code exercise is to calculate the factorial of given number by the user