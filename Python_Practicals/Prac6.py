#Write a python program to read height in cm and then convert it in feet and inches
def Converter(CM):
    Inches = CM * 0.393701
    Feet = CM * 0.0328084
    print("Converted Values")
    print("Inches: ",round(Inches, 3))
    print("Feet: ",round(Feet, 3))
Centimeter = float(input("Enter Centimeters: "))
Converter(Centimeter)
