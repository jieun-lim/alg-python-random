"""
목표: 최대 예쁨값 구하기

화장실 크기: 2*N
2x1크기의 타일 A(1x2도 된다), 2x2의 타일 B개

# 2xB + A >= N??

1<=예쁨 <= 10**6



"""


"""
그리디? 
A, B 리스트를 정렬 (오름차순)

1. 제일 큰 요소를 순차적으로 꺼냄. 

2. 2x2일 경우 1x2에서 대체할 수 있는 것이 있는지 파악
   - N이 짝수인 경우 - 상관 없음
   - N이 홀 수인 경우 - 1x2가 적어도 1개 남아 있는지 확인   
   => 대체할 수 있으면 대체
"""




"""
예외 상황 
N이 홀수인데, A가 짝수 -> 0 
N이 짝수인데, A가 홀수 -> 0 

e.g. 
N = 10
A = 2
B = 4
2xB + A > 10
-> 예외 없이 무조건 채워진다는 거네..? 
"""


N, A, B = map(int, input().split()) # 1 <= N, A, B <= 2000

stack_A = list(map(int, input().split()))
stack_B = list(map(int, input().split()))

stack_A.sort() # 오름차순 정렬
stack_B.sort() # 오름차순 정렬
ans = 0
res_col = N
while stack_A and stack_B and res_col > 0: # 아직 배치할 도형이 둘 다 남아 있을 때
    if stack_A[-1] <= stack_B[-1]: # 2x2의 가중치가 더 클 때
        if res_col >= 2:
            if len(stack_A) >= 2 and (stack_A[-1] + stack_A[-2]) > stack_B[-1]:
                ans += stack_A.pop()
                ans += stack_A.pop()
            else:
                ans += stack_B.pop()
            res_col -= 2
        else:
            ans += stack_A.pop()
            res_col -= 1
    else:
        ans += stack_A.pop()
        res_col -= 1

print(ans)




# 배치를 통해서, 도형이 채워질 수 있는가?






