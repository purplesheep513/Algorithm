import sys
from collections import deque

M,N = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

days = [0]

queue = deque([])
for a in range(N):
    for b in range(M):
        if graph[a][b]==1:
            queue.append((a,b))
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <N and 0<= ny <M and graph[nx][ny] ==0:
            days.append(graph[x][y])
            graph[nx][ny] = graph[x][y] +1
            queue.append((nx,ny))
            

no_ripe = False
for i in range(N):
    for j in range(M):
        if  graph[i][j] == 0:
            no_ripe = True
            break

if no_ripe:
    print(-1)
else:
    print(max(days))