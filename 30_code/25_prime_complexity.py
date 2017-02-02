from math import sqrt


T = int(input())
n = [int(input()) for i in range(T)]
for num in n:
    if not num % 2 and num > 2 or num == 1:
        print('Not prime')
        continue
    if all(num % i for i in range(3, int(sqrt(num)) + 1, 2)):
        print('Prime')
    else:
        print('Not prime')
