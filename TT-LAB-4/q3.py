def letterCount(myStr, letter):
    count = 0
    for i in myStr:
        if letter == i:
            count = count + 1
    return count

print("Enter string: ", end="")
myStr = input()
print("Enter the letter: ", end="")
letter = input()
print("Count of the letter: " + str(letterCount(myStr, letter)))