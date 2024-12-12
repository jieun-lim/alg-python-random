"""
N일 동안 M명이 불침번을 선다.
1일에 1번씩, 반복할 숭 ㅣㅆ음.

3일 2명

N=5, M = 3
5*5*5*5*5


"""
import math
N, M = map(int, input().split())

ans = (M**N - (M-1)**(N)) % 1000000007
# ans = (math.pow(M,N) - math.pow(M-1, N)) % 1000000007
print(int(ans))

