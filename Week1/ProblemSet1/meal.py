def main():
    clock = convert(input("What time is it? "))
    
    if 7 <= clock <= 8:
        print("breakfast time")
    elif 12 <= clock <= 13:
        print("lunch time")
    elif 18 <= clock <= 19:
        print("dinner time")
    else:
        pass




def convert(time):
    hours, minutes = time.split(":")
    tenth = int(minutes)/60
    return int(hours) + tenth

if __name__ == "__main__":
    main()