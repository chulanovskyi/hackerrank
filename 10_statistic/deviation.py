from math import sqrt
n = int(input())
X = [int(i) for i in input().strip().split(' ')]
avg = int(sum(X)/n)
distance = int(sum([int((i-avg)**2) for i in X])/n)
deviation = round(sqrt(distance), 1)
print(deviation)
