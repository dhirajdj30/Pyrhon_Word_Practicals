# Write a program to calculate perimeter and volume of the cone
from cmath import pi


Height = int(input("Enter Height of the Cone: "))
Radius = int(input("Enter Radius of the Cone: "))
Perimeter = 2*pi*Radius
print("Perimeter of the Cone is : ", Perimeter)
Volume = (1/3)*pi*(Radius*Radius)*Height
print("Volume of the Cone is : ",Volume)
