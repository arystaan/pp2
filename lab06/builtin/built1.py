from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = map(int, list(input().split()))
print(multiply_list(numbers))  