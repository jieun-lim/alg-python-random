"""
문제: 모든 학생들의 시야가 확보되도록 좌석 배치할 수 있는지 여부를 판단하기("YES" or "NO")
- 앞 좌석 (좌석 높이+ 키) < 나의 (좌석 높이+키)
<좌석 배치>
- N행 M열의 좌석이 있음.

<행 높이>
- 높이가 D부터 시작
- i(1,,,N) -> 높이가 D*i

"""

"""
어떻게 판단할 수 있을 것인가? 
앞 행의 같은 열에 있는 모든 학생들 보다 키가 커야된다. 

일단 각 학생의 키: D*(i)+h[i][j]
앞 좌석에 있는 학생의 키: D*(i-1)+h[i-1][j]
----------------
어떻게 배치할 수 있을 것인가? 
행 단위 정렬? 

예시1) 
3행: 5 2 2
2행: 4 1 4
1행: 1 2 5
<더함>
3행: 11 8 8 
2행: 7 4 7
1행: 1 2 5


3행: 11 8 8
2행: 4 4 7
1행: 1 2 5


예시2) 
2 1 5
8
2



예시1) 3 3 3
3행: 1 2 4
2행: 4 5 3
1행: 1 2 3

"""


# 입력 받기
N, M, D  = list(map(int, input().split()))

h = [[-1]*(M+1)] # # N이랑 M이 1부터 시작할 수 있게 한다.
for _ in range(N):
    h.append([-1]+list(map(int, input().split())))

def accumulate(h, D): # 높이 더해주기
    for i in range(1,N+1):
        for j in range(1,M+1):
            h[i][j] += i*D
    return h

def sort_by_row(h):
    # 행 단위로 오름차순 정렬하기
    for i in range(1, N + 1):
        h[i].sort()
    return h

def available(h):
    # 각 열 단위로 앞 행의 모든 원소들이 나보다 작은지 체크하기
    for j in range(1, M + 1):
        for i in range(1, N):
            if h[i][j] >= h[i+1][j]: # (i-1) 번째 행이
                return False
    return True

# print('\n'.join(map(str, h)))
h = accumulate(h, D)
h = sort_by_row(h)
result = available(h)

if result:
    print("YES")
else:
    print("NO")

"""
1 3 5
1 2 3
-> 
3
8
11
"""

