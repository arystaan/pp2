# 1)
# n = int(input("Enter number: "))
# def sqr():
#     for i in range(1, n + 1):
#         yield i ** 2
# for i in sqr():
#     print(i)

# 2)
# def ev_num(n):
#     for i in range(0, n+1, 2):
#         yield str(i)
# n = int(input("Enter number: "))
# ev_num = ev_num(n)
# result = ','.join(ev_num)
# print(result)

# 3)
# def divisible(n):
#     for i in range(0,n+1):
#         if i%3 == 0 and i%4 == 0:
#             yield i
# n=int(input())
# for a in divisible(n):
#     print(a)

# 4)
# a = int(input())
# b = int(input())
# def squares():
#     for i in range(a, b + 1):
#         yield i ** 2
# list = []
# for i in squares():
#     list.append(str(i))
# print(",".join(list))

# 5)
# n = int(input("Enter number: "))
# def down():
#     cnt = 0
#     while cnt <= n:
#         if n == 0:
#             yield 0
#             break
#         else:
#             yield n - cnt
#             cnt += 1
# list = []
# for i in down():
#     list.append(str(i))
# print(",".join(list))
 