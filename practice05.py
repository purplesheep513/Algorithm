import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(N):
    graph.append(list(sys.stdin.readline()))

visit = [[-1 for _ in range(M)] for _ in range(N)]

def bfs(x,y):
    global N, M
    queue = deque([(x,y)])
    visit[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx and nx<N and 0<=ny and ny<M:
                if visit[nx][ny] == -1 and graph[nx][ny] == "1":
                    visit[nx][ny] = visit[x][y] + int(graph[nx][ny])
                    queue.append((nx,ny))

bfs(0,0)

print(visit[N-1][M-1])