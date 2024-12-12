
def find_level(N:int) -> int:
    """
    몬스터 킬수가 들어오면 몇 레벨 상승했는지 이분 탐색으로 반환해주는 함수
    - 경험치의 합:  n(n+1)
    :param N:
    :return:
    level: 상승 레벨 수
    """
    cur_exp = N * (N + 1) // 2 # 현재 나의 경험치 누적값, N은 죽인 몬스터의 수
    l, r = 1, 10**9
    level = 0
    while l <= r:
        m = (l + r) // 2
        need = m*(m + 1)
        if cur_exp >= need: # 경험치가 충분하면 더 높은 레벨로 업뎃 가능
            level = m
            l = m + 1
        else:
            r = m - 1
    return level

T = int(input()) # 테스트 케이스의 수 1<=T<=1000
for _ in range(T):
    N = int(input()) # 1 <= N <= 10**9
    level_d = find_level(N)
    print(level_d+1)

