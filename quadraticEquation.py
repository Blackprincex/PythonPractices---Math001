import cmath as c

print("Quadratic Equation solver")
print("ax^2 + bx + c = 0")

cofA = float(input("What is the value of a : "))
cofB = float(input("What is the value of b : "))
cofC = float(input("What is the value of c : "))

discriminant = cofB**2 - 4 * cofA * cofC

x1 = (-cofB + c.sqrt(discriminant)) / 2 * cofA
x2 = (-cofB - c.sqrt(discriminant)) / 2 * cofA

print("The root X1 of the equation is ", x1)
print("The root X2 of the equation is ", x2)
