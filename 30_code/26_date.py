from datetime import datetime


actual = datetime(*list(map(lambda i: int(i), input().strip().split()))[::-1])
expected = datetime(*list(map(lambda i: int(i), input().strip().split()))[::-1])

def calc_fine(act, exp):
    if act.year > exp.year:
        return 10000
    elif act.year < exp.year or act.month < exp.month:
        return 0
    if act.month > exp.month:
        return (act.month - exp.month) * 500
    else:
        if act.day > exp.day:
            return (act.day - exp.day) * 15

print(calc_fine(actual, expected))

