import math, time
def rootWithDelay(x, delay):
    time.sleep(delay/1000)
    return math.sqrt(x)
print("Input:")
x = int(input())
delay = int(input())
print(f"Output:\nSquare root of {x} after {delay} miliseconds is {rootWithDelay(x, delay)}")