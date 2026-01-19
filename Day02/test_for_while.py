# def find_primes(n):
#     primes = []
#     for num in range(2, n + 1):  # 从2开始到n
#         is_prime = True
#         # 检查num是否为质数
#         for i in range(2, int(num ** 0.5) + 1):  # 只需检查到sqrt(num)
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
#
#
# primes_up_to_500 = find_primes(500)
# print(primes_up_to_500)

# 查找1到500之间的所有质数
primes = []
for num in range(2, 500 + 1):  # 从2开始到n

    is_prime = True
    # 检查num是否为质数
    for i in range(2, int(num ** 0.5) + 1):  # 只需检查到sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)
print(len(primes))

# import math
# i = 1
# while i < 500:
#     is_prime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime and i > 1:
#         print(i)
#     i += 1



