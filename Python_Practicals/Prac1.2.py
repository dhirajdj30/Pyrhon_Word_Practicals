from typing import Tuple


Sr_no = 29
ID_CODE = 19029
Name = "Dhiraj Madhukar Jagtap"
Branch = "Computer"
Sub = ['Python','Linux','CG', "Cloud Computing",'ETCE']
Branches = ('IT','CM','CE','ETC','EE','ME')
#Printing the type of the Identifiers
print(ID_CODE, type(ID_CODE))
print(Sr_no, type(Sr_no))
print(Name, type(Name))
print(Branch, type(Branch))
print(Sub, type(Sub))
print(Branches, type(Branches))
#Type casting
print(float(Sr_no))
print(str(ID_CODE))
print(list(Name))
print(tuple(Sub))
print(list(Branch))