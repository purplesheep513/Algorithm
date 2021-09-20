# 정리해보자

# 1. 수빈이와 동생은 1차원 배열에서 움직인다.
# 2. visit 배열을 만들어서 수빈이가 움직이는 좌표의 최단시간를 저장한다.
#     -bfs의 가장 좋은점은 반드시 최단시간(또는 최단거리)만 저장된다는 점이다
# 3. visit 의 범위는 수빈이의 위치를 넘어갈 수도 있다(N+1, 2*N 때문)

# ※ 가장 중요한 부분은 visit 배열의 값은 각 좌표의 최단시간을 나타낸다는 것이다.
# (예:visit[3] == 1 일경우 수빈이가 3을 방문했을 때의 최단시간이 1초라는 뜻)
    

import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split())
visit = [0 for _ in range(100001)]
def bfs(N):
    global M
    queue = deque([N])
    visit[N] = 0
    while queue:
        N = queue.popleft()
        if N != M:
            x = N-1
            if 0<=x<100001 and visit[x] == 0:
                visit[x] = visit[N] + 1
                queue.append(x)

            x = N + 1
            if 0<=x<100001 and visit[x] == 0:
                visit[x] = visit[N] + 1
                queue.append(x)

            x = 2 * N
            if 0<=x<100001 and visit[x] == 0:
                visit[x] = visit[N] + 1
                queue.append(x)
        elif N == M :
            print(visit[N])
            break

bfs(N)