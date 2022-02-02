def addOddEven(VALUES):
    e, o = 0, 0
    for i in VALUES:
        if i%2 == 0:
            o = o + i
        else:
            e = e + i
    print("Even Sum: " + str(o) + " Odd Sum: " + str(e))

print("Enter the list size: ", end="")
n = int(input())
print("Enter the elements: ")
VALUES = []
for i in range(0, n):
    VALUES.append(int(input()))
addOddEven(VALUES)