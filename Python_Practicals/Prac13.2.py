#Aim:  To  read age  of  15  person and  count total Baby age, School age  and  Adult age. 

age= 0
cnt_baby=0
cnt_school=0
cnt_adult=0
count=0
while (count != 15):
    age = int(input("Enter the age of the person: "))
    if (age <= 5):
        cnt_baby = cnt_baby + 1
    elif(age < 18):
        cnt_school = cnt_school + 1
    elif(age > 18):
        cnt_adult = cnt_adult + 1
    count = count + 1
print("Total Numbers of Baby: ",cnt_baby)
print("Total Numbers of School age: ",cnt_school)
print("Total Numbers of Adult age: ", cnt_adult)
