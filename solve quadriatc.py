import cmath
## solve quadratic
A = int(input("What is your A varible? "))
B = int(input("What is your B varible? "))
C = int(input("What is your C varible? "))
print(-B + cmath.sqrt(B**2 - 4 * A * C) / 2 * A)
print(-B - cmath.sqrt(B**2 - 4 * A * C) / 2 * A)