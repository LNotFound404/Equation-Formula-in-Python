import math


def formula():
    s = b**2 - 4 * a * c
    x = (-(b) + math.sqrt(s)) / (2 * a)
    print(f"pos: {x}")
    x = (-(b) - math.sqrt(s)) / (2 * a)
    print(f"neg: {x}")

a = float(input("enter value a: "))
b = float(input("enter value b: "))
c = float(input("enter value c: "))

try:
    formula()
except ValueError:
    print("error")