def showlarge(s):
    l = s.split(" ")
    for i in l:
        if len(i) > 4:
            print(i)

print("Enter string: ", end="")
myStr = input()
print()
print("Strings with char count more than 4 are:")
showlarge(myStr)