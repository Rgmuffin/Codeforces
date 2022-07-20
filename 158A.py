'''
https://codeforces.com/problemset/problem/158/A
'''

n, k = input().split()
numbers = list(input().split())
next_round = 0
pos = int(numbers[int(k)-1])

for i in numbers:
    print('i', i)
    print('pos', pos)
    if int(i) >= pos and int(i) > 0:
        next_round += 1

print(next_round)