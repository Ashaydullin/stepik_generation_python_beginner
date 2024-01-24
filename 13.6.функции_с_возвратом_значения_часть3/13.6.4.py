from math import*
def get_circle(radius):
    return 2*pi*radius, pi*(radius**2)

r = float(input())

length, square = get_circle(r)
print(length, square)