lst = list(map(int, input().split()))
primes = filter(lambda x: all(x%i != 0 for i in range(2, x)), lst)
result = list(primes)
if 1 in result:
    result.remove(1)
print(result)