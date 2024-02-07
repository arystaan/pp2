def has_33(arr):
    count = 0
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1] == 3):
            count+=1
        if count >= 1:
            return True
    return False

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(has_33(numbers))