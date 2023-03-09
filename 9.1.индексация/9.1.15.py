num = int(input())  
double = ""            
while num > 0:
    double += str(num % 2)   
    num //= 2
print(double)