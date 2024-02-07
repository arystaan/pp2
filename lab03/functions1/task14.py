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

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chicken = numheads - rabbits
    print(int(rabbits), int(chicken))

inp = input()
x, y = map(int, inp.split())
solve(x, y)

"""
from spy_game import spy_game
from heads_and_legs import solve
n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))

inp = input()
x, y = map(int, inp.split())
solve(x, y)
"""
