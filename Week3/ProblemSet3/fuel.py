while True:
    try:
        x = input("Enter the fuel gauge: ")
        a, b = x.split("/")
        a = int(a)
        b = int(b)
        y = a / b * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if a <= b and a >= 0:
            if y >= 99:
                print("F")
            elif y <= 1:
                print("E")
            else:
                print(round(y), "%", sep="")
            break
        else:
            pass
