from collections import Counter

s = input()
letters = Counter(s.lower())
del letters[' ']
is_pangram = (len(letters.keys()) == 26)
if is_pangram:
    print('pangram')
else:
    print('not pangram')
