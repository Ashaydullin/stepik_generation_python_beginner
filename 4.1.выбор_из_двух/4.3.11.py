age = int(input())
if age <= 13:
    print('детство')
else:
    if age >= 14 and age <= 24:
        print('молодость')
    else:
        if age >= 25 and age <= 59:
            print('зрелость')
        else: 
            if age >= 60:
                print('старость')

# Но лучше вот так

age = int(input())
if age <= 13:
    print('детство')
elif age >= 14 and age <= 24:
    print('молодость')
elif age >= 25 and age <= 59:
    print('зрелость')
elif age >= 60:
    print('старость')