#Practical 3: Find the average of the given list
def Average(list):
    Sum = sum(list)
    Length = len(list)
    Avg = Sum/Length
    print('Average of given List is',Avg)
Percent = [93.4, 96.3, 97.5, 98.2, 89.2]
Name_len = [1000,50020,6102,4515,121]
Average(Percent)
Average(Name_len)