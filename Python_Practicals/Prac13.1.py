#Aim: print all  prime numbers from 1  to  N. 
def PrimeChecker(a):  
      
    if a > 1:    
        for j in range(2, int(a/2) + 1):  
            if (a % j) == 0:   
                break  
        else:  
            print(a)  
      

N = int(input("Enter the range: "))

for i in range(0,N+1):
    PrimeChecker(i)  