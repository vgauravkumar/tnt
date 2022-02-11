tot = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

f = open("Q1.txt", "r")
content = f.read()
for ch in content:
    if ch.lower() in vowels:
        tot+=1


print("\nTotal Vowels are:")
print(tot)
f.close()