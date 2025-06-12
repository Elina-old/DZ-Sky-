import math


def square(side):
    return math.ceil(side * side)


num_side = int(input("сторона квадрата: "))
print(f"площадь квадрата: {square(num_side)}")
