"""
1936. 1대 1 가위바위보
"""

import sys
sys.stdin = open('1936_input.txt')

A, B= map(int, input().split())
print(A, B)

if A == 1:
    if B==2:
        print('B')
    else:
        print('A')
elif A == 2:
    if B == 1:
        print('A')
    else :
        print('B')
else :
    if B == 1:
        print('B')
    else :
        print('A')
