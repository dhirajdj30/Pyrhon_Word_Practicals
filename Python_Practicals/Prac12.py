# Write a program to create dictionry, Add element to the dict, Delete element from the dict.
def AddDictElement():
    key = str(input("Enter the Key for the Subject: "))
    Marks = int(input("Enter the marks of the subjects: "))
    Dict[key]= Marks
    print("Dict: ",Dict)
def DelDictElement(Code):
    Dict.pop(Code)
    print("Dict: ", Dict)
Dict = {'LX':75, 'CC':98, 'PY': 87, 'CG':95}
Los = 0
while Los != 4:
    print("1. Add Item to Dict..")
    print("2. Delete Item From Dict..")
    print("3. Print the Dict")
    print("4. EXIT")
    Choice = int(input("Enter Your Choice 1-4: "))
    if(Choice == 1):
        AddDictElement()
    elif(Choice==2):
        CD = str(input("Enter the key of the item: "))
        DelDictElement(CD)
    elif(Choice == 3):
        print("Dict: ", Dict)
    elif(Choice == 4):
        Los = 4
    else :
        print("Enter an appropriate option: ")

