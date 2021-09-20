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
