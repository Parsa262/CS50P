# gets input and uses convert function 
def main():
    text = input("Input: ")
    results = convert(text)
    print(results)

# converts emotes to emojies and returns the value of the converted text
def convert(to):
    to = to.replace(":)","🙂")
    to = to.replace(":(","🙁")
    return to
    
main()