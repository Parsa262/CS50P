s = input("Write: ")

for c in s:
    if c.lower() in "aeiuo":
        print("", end="")
    else:
        print(c, end="")