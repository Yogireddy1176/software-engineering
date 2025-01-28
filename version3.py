import math

# Read coefficients from a file
with open("input_single.txt", "r") as file:
    a, b, c = map(float, file.readline().split())

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
