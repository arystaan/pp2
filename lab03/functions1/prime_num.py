import math
def filter_prime(lst):
    primes = []
    for x in lst:
        if x < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

print(filter_prime(numbers))