"""
목적: 주어진 이동 조건에 따라서 쩰리가 우승할 수 있는지 알아보기
점프
- 시작점(0,0)
- 이동 조건
  - 이동 방향: 오른쪽(0,+1) or 아래 (-1,0)
  - 이동 크기: 현재 밟고 있는 칸의 수 만큼 (0~100)
  - 이동 제한: NxN 맵 밖으로 나가면 안됨.
승리 조건: (N-1,N-1)로 도달

입력:
- N(2<= N <= 64)
- NxN 크기의 맵
  - 승리 지점: -1, 나머지는 0~100의 정수
출력: 우승할 수 있으면 HaruHaru, 아니면 Hing
"""

"""
내가 선택한 알고리즘: 완전 탐색 & 백트래킹 
그 이유는? N <= 64이다. 
모든 칸(64*64)에 대해서 2(2방향)으로 이동 -> O(64*64*2)
"""

"""
예시1) 
3
1 1 10
1 5 1
2 2 -1

3
(1) 1 10
(1) 5 1
(2) 2 (-1)
경로: 1-1-2-(-1)

- (0,0)  +  (0,1)
- (1,0) /  (0,1) / + (1,2), (2,0)
- (0,1) / (1,2), (2,0) / + (1,2) (0,2)
- (1,2) / (2,0) (1,2) (0,2) / + --
 -(2,0) / (1,2) (0,2) / + (2,2)
 - (1,2) / (0,2) (2,2) / + (2,2), 
- (0,2) (2,2) / + (2,2), 
---------

예시2) 
3
2 2 1
2 2 2
1 2 -1

"""


"""
모든 경우의 수를 다 따져보기
queue에 시작점 넣기 
우승 여부 = False
while queue: # 큐가 빌 때까지 
    # queue.pop()이 도착점이면 우승 -> 우승 여부 = True & 종료 
    # 아니면 
    현재 칸의 개수*모든 이동 방향으로 이동하기!
    벗어나지 않았을 경우에만 큐에 넣기 
"""

from collections import deque

# 입력 받기
N = int(input()) #  2<= N <= 64
board = [list(map(int, input().split())) for _ in range(N)] # NxN 크기의 게임맵

def out_of_range(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    return False

def check(N, board) -> bool:
    answer = False
    queue = deque()
    queue.append((0, 0))
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True
    d_lst = [(0,+1),(+1,0)] # 오른쪽, 아래 이동
    while queue: # 큐가 빌 때까지
        x,y = queue.popleft()
        if x == N-1 and y == N-1:
            answer = True
            break
        for dx,dy in d_lst:
            amount = board[x][y]
            nx, ny = x+(dx*amount), y+(dy*amount)
            if not out_of_range(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return answer

result = check(N,board)
if result: print("HaruHaru")
else: print("Hing")

"""
예외 처리

# case1 : 움직일 수 없는 경우  
3
0 0 0
0 0 0
0 0 -1
False

# case2: 이동 방향이 100인 경우 
3
100 0 0
0 0 0
0 0 -1

# case3: 64x64
N = 64
board = [ list(range(0,64)) for _ in range(N)]

경로가 겹치는 경우가 있나요?
그 지점에 왔으면 경로가 겹쳐도 같은 방향으로 가게 됨!!
그니까 방문 처리를 해도 된다. 
 
"""





