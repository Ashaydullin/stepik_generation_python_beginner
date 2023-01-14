month = int(input())
if month == 2:
    print("28")        
elif month <= 7:            
    print(30 + month%2 )    
else: 
    print(31 - month%2 )