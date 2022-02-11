count = 0
f = open("Q2.txt", "r")
content = f.read()
for word in content.split():
    if word.lower() == "the":
        count+=1
print(count)