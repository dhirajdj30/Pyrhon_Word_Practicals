#Write a python program to merge two list and Sort it
List1 = []
List2 = []
NE1 = int(input("Enter number of element in the first list: "))
for i in range(0,NE1):
    Ls1 = int(input("Enter Elements: "))
    List1.append(Ls1)
    print(List1)
NE2 = int(input("Enter number of element in the second list:"))
for i in range(0,NE2):
    Ls2 = int(input("Enter Elements "))
    List2.append(Ls2)
    print(List2)
MergedList = List1 + List2
print()
print("Merged List",MergedList)
MergedList.sort()
print()
print("Sorted Merged List: ",MergedList)
