def showlarge(s):
    l = s.split(" ")
    for i in l:
        if len(i) > 4:
            print(i)
s = input()
showlarge(s)