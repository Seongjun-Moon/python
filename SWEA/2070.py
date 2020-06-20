"""
2070. 큰 놈, 작은 놈, 같은 놈
"""

import sys
sys.stdin = open('2070_input.txt')

TC = int(input())

for i in range(1, TC+1):
    a, b = list(map(int, input().split()))
    sign = ''
    if a>b:
       sign = '>'
    elif a < b:
        sign = '<'
    else:
        sing = '='
    print(f'#{i} {sign}')  

