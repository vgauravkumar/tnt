def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

print("Enter the list size: ", end="")
n = int(input())

print("Enter the elements: ")
myList = []
for i in range(0, n):
    myList.append(int(input()))

print("Enter the element you want to search: ", end="")
x = int(input())
result = binary_search(myList, 0, len(myList)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")