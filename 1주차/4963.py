"""
섬의 개수

같은 섬: 상,하, 좌, 우, 대각선
1: 땅, 0은 바다

"""
from collections import deque
def BFS(board, i, j):
    d_lst = [(0,1),(0,-1),(1,0),(-1,0), (+1,1),(+1,-1),(-1,1),(-1,-1)]
    global visited
    queue = deque()

    visited[i][j] = True
    queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for dx, dy in d_lst:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= h or ny<0 or ny>=w:
                continue
            if not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

while True:
    global visited
    # 입력 받기
    w, h = list(map(int, input().split()))  # w: 열의 개수, h: 행의 개수, 1<=w,h<=50
    if w == 0  and h == 0:  break
    board = [list(map(int,input().split())) for _ in range(h)]
    # 검사
    visited = [[False]*w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == 1:
                BFS(board,i,j)
                ans += 1
    print(ans)









