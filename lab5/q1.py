f = open("Q1.txt", "r")
content = f.read()
for word in content.split():
    if word[0].lower() == "s":
        print(word)