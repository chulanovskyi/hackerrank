#!/bin/python3


n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())

    qualifier = grade % 10
    up_range = [3,4,8,9]
    if qualifier in up_range and grade > 37:
        upgrade = grade - (qualifier % 5) + 5
        print(upgrade)
    else:
        print(grade)
