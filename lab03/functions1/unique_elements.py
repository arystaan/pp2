def unique_elems(arr):
    lst = []
    for i in arr:
        if i not in lst:
            lst.append(i)
    return lst

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(unique_elems(numbers))
 