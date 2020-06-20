"""
2029. 목과 나머지 출력하기
"""

import sys
sys.stdin = open('2029_input.txt')

TC = int(input())

for i in range(1, TC+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')