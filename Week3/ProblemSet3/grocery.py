items = []
while True:
    try:
        item = input("").upper()
        items = items + [item]
    except EOFError:
        counts = {}
        for item in items:
            if item in counts:
                counts[item] += 1 
            else:
                counts[item] = 1
        for item in sorted(counts):
            print(counts[item], item)
        break