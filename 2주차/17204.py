"""
보성이가 벌주를 먹게 하기 위해서 영기가 불러야하는 최소의 양수 M을 찾기
- 자기 자신을 지목하는 경우
- 영기가 항상 0번
"""


"""
예시1) 

       0
    4     1
    3(보) 2
앉은 순서: 0 1 2 3 4
지목 상대 1 3 2 1 4

       0
    4     1
    3(보) 2


지목 순서 1 3 2 1 4

--------
1 3 5 4 0 2

0 -> 1 -> 3 -> 4-> 0 -> 1
    
"""

# 입력 받기
N, K = map(int, input().split()) # N(참여자) 3<=N<=150, 보성이의 번호
next_lst = []
for _ in range(N): next_lst.append(int(input()))


# Body
prev = 0 # 시작 인덱스
ans = -1
for i in range(N):
    next_ = next_lst[prev]
    if next_ == K: # 보성이를 찾음
        ans = i+1
        break
    elif prev == next_: # 자기 자신을 지목했을 때
        break
    prev = next_
print(ans)




