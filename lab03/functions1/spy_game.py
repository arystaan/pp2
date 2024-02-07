def spy_game(arr):
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == 0 and arr[i+2] == 7:
            return True
        else:
            continue
    return False


n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))