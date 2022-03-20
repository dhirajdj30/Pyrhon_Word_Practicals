#Write a Python Program to find the Sum of the digits in the number

Num = int(input("Enter a Number: " ))
Total = 0 
while(Num>0):
    Digit = Num % 10
    Total = Total + Digit
    Num = Num//10
print("The Sum of the Digits: ", Total)























