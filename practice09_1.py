import sys
from collections import deque

N,M = map(int,sys.stdin.readline().rstrip().split())
visit = [0 for _ in range(1000001)]

def bfs(x):
    global M
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == M :
            print(visit[x])
            break
        for nx in [x+1, x-1, 2*x]:
            if 0 <= nx < 1000001 :
                if visit[nx] == 0 :
                    visit[nx] = visit[x] + 1
                    queue.append(nx)

bfs(N)
