def oddtoeven(L):
    for i in range(0, len(L)):
        if L[i]%2 != 0:
            L[i] = L[i]*2
    return L

print("Enter the list size: ", end="")
n = int(input())
print("Enter the elements: ")
kritikaList = []
for i in range(0, n):
    kritikaList.append(int(input()))
oddtoeven(kritikaList)
print(kritikaList)