# making a string
string = "Hello World"
print(string)

# string length
length = len(string)
print(length)

# Accessing single characters
char = string[0]
print(char)

# Accessing substrings
substr = string[1:3]
print(substr)

# Finding a string
findstr = string.find("Hellnnno")
print(findstr)

# Counting 
countstr = string.count("l")
print(countstr)

# Lower case
lowerstr = string.lower()
print(lowerstr)

# Replacing String
replacestr = string.replace("Hello", "*****")
print(replacestr)

# Starts with
ifstrstartwith = string.startswith("G")
print(ifstrstartwith)