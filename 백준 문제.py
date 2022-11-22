# 입력받는 함수
# import sys
# sys.stdin.readline()  

# 여러개 입력 받기
# n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]  

import sys

data = [int(sys.stdin.readline().strip()) for i in range(1,9)]

a = set(data)
b = set(list(range(1,11)))
list(b.difference(a)).sort()

for i in list(b.difference(a)):
    print(i)
