import math


def square(items):
    return math.ceil(items * items)


num_items = int(input("сторона квадрата: "))
print(f"площадь квадрата: {square(num_items)}")
