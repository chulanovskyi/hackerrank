n = int(input())
X = [int(i) for i in input().strip().split(' ')]
F = [int(i) for i in input().strip().split(' ')]
num_freq = list(zip(X, F))
num_freq.sort()
S = [[num for i in range(freq)] for num, freq in num_freq]
S = [x for sublist in S for x in sublist]

half = int(len(S)/2)
quarter = int(half/2)

left = S[:half]
right = S[:half:-1]
if half%2:
    L = left[quarter]
    R = right[quarter]
else:
    L = round(sum(left[:quarter+1][-2:])/2, 1)
    R = round(sum(right[:quarter+1][-2:])/2, 1)
interquartile = round(float(R-L), 1)
print(interquartile)
