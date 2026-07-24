months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("What's the date? ")
        if "/" in date:
            mm, dd, yyyy = date.split("/")
            dd = int(dd)
            mm = int(mm)
            yyyy = int(yyyy)
            if 1 <= mm <= 12 and 1 <= dd <= 31 and mm not in months:
                print(f"{yyyy:04}-{int(mm):02}-{dd:02}") 
                break
            else:
                pass
        else:
            mm, dd, yyyy = date.split(" ")

            if mm in months and "," in dd:
                dd = dd.replace(",", "")
                mm = months.index(mm) + 1
                dd = int(dd)
                yyyy = int(yyyy)

                if 1 <= dd <= 31:
                    print(f"{yyyy:04}-{mm:02}-{dd:02}")
                    break
                else:
                    pass
    except (ValueError, TypeError):
        print("Error")