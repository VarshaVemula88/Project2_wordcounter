def WordCounter(text:str) -> int:
    # getting sentences
    lines = text.split("\n")

    words = []
    for line in lines:
        # words from sentences
        print(line)
        for word in line.split(" "):
            words.append(word)
    return len(words)

# taking multiline input
lines = []
print("Please Enter your text: ")
while True:
    line = input()
    if not line:
        break
    lines.append(line)

# providing the string of input to the WordCounter function
words = WordCounter(str(lines))
print(f'Your text has {words} words.')