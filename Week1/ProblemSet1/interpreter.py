expression = input("Type in your arithmetic expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "/":
    a = x / z
    print(f"{a:.1f}")
elif y == "+":
    a = x + z
    print(f"{a:.1f}")
elif y == "-":
    a = x - z
    print(f"{a:.1f}")
elif y == "*":
    a = x * z
    print(f"{a:.1f}")
else:
    pass