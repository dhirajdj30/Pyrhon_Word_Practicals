# Write a peogram to Do Various operation on list 
Company = []
Los = 0
while Los != 7:
    print("1. Add Item to list..")
    print("2. Delete Item From list..")
    print("3. Reverse the list..")
    print("4. Sort Items of list..")
    print("5. Count Items in the List..")
    print("6. Clear all Items from list")
    print("7. Print the List")
    print("0. EXIT")
    Choice = int(input("Enter Your Choice 1-7: "))
    if(Choice == 1):
        Com = str(input("Enter the item name: "))
        Company.append(Com)
    elif(Choice==2):
        Com = str(input("Enter the item name: "))
        Company.remove(Com)
    elif(Choice == 3):
        Company.reverse()
    elif(Choice == 4):
        Company.sort()
    elif(Choice == 6):
        Company.clear()
    elif(Choice == 5):
        Com = str(input("Enter the item name: "))
        print("Number of the item specified: ",Company.count(Com))
    elif(Choice == 7):
        print(Company)
    elif(Choice == 0):
        Los = 7
    else:
        print("Enter Appropriate option..")
print(Company)