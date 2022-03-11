# Aim: Write a python program to exchange value of two numbers without using tempeory variable
var1=int(input("Enter value of first variable: "))
var2=int(input("Enter value of second variable: "))
var1= var1+var2
var2 = var1-var2
var1= var1-var2
print("a is:",var1," b is:",var2)