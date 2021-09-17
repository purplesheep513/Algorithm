import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
for _ in range(edge):
    c, e = map(int,sys.stdin.readline().rstrip().split())
    graph[c].append(e)
    graph[e].append(c)

visit = [0 for _ in range(N+1)]

def bfs(x) :
    cnt = 0
    visit[x] = 1
    queue = deque([x])
    while queue :
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = 1
                cnt +=1
                queue.append(i)
    print(cnt)

bfs(1)