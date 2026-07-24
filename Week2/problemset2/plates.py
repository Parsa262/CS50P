def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")    


def is_valid(s):

    digit = False
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    for c in s:
        if not c.isalnum():
            return False
    for c in s:
        if c.isdigit():
            if not digit:
                if c == "0":
                    return False
                digit = True
        elif digit and c.isalpha():
            return False
    return True
            

main()