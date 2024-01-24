def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

print(*get_middle_point(
    int(input()), 
    int(input()), 
    int(input()), 
    int(input())))