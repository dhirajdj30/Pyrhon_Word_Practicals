#write a Python program to print all numbers dividible by a given number
Num = int(input("Enter the number: "))
highest = int(input("Enter the highest range of the number: "))
for i in range(1,highest+1):
    if(i%Num == 0):
        print(i)
