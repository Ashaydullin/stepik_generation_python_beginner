witchprice = int(input())
witchcounter = 0
while witchprice > 0: 
    if witchprice >= 25:
        witchprice -= 25  
    elif witchprice >= 10:
        witchprice -= 10    
    elif witchprice >= 5: 
        witchprice -= 5     
    else:            
        witchprice-=1     
    witchcounter += 1         
print(witchcounter)  
