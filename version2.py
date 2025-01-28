import math

# Getting coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solving the quadratic equation
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"Root: {root:.2f}")
else:
    print("No real roots.")
