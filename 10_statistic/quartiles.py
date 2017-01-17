n = int(input())
arr = [int(i) for i in input().strip().split(' ')]
half = int(n/2)
quarter = int(half/2)
arr.sort()

if n%2:
    X = arr[half]
else:
    X = int(sum(arr[:half+1][-2:])/2) 

left = arr[:half]
right = arr[:half:-1]
if half%2:
    L = left[quarter]
    R = right[quarter]
else:
    L = int(sum(left[:quarter+1][-2:])/2)
    R = int(sum(right[:quarter+1][-2:])/2)

print('Arr: ', arr)
print('Left: ', left)
print('Right: ', right)
print('X: ', X)
print(L)
print(X)
print(R)
