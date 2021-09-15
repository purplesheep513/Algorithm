import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = []
visit = [[-1 for _ in range(N)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

total = 0
regi = []

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

def bfs(x,y):
    queue = deque([(x,y)])
    cnt = 0
    if graph[x][y] != "0":
        cnt +=1
        visit[x][y] = 0
        queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visit[nx][ny] == -1 and graph[nx][ny] == "1":
                    visit[nx][ny] = 0
                    cnt += 1
                    queue.append((nx,ny))
    if cnt != 0:
        regi.append(cnt)

for i in range(N):
    for j in range(N):
        if visit[i][j] == -1 and graph[i][j] != "0":
            total +=1
            bfs(i,j)

print(total)
regi.sort()
for i in regi:
    print(i)