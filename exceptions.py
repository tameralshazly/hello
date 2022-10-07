import sys

try:
    x = int(input("X: "))
    y = int(input("Y: " ))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)
    
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can not divide by Zero.")
    sys.exit(1)

print(f"{x} / {y} is equal to {result}")