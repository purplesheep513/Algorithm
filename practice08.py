import sys
from collections import deque
import copy

M,N = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().rstrip().split()))

graph2 = copy.deepcopy(graph)
visit = [[0 for _ in range(M)] for _ in range(N)]
visit2 = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    visit[x][y]=1
    queue = deque([(x,y)])
    if graph[x][y] != 0:
        queue.popleft()
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0 <= ny < M: 
                if graph[nx][nx]==0:
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append((nx,ny))

def ripe(x,y):
    visit2[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0 <= ny < M :
            if visit2[nx][ny] == 0 :
                if graph[x][y]==1 and graph[nx][ny] ==0:
                    graph2[nx][ny] = 1

cnt = 0
day = 0

while True:
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and graph[i][j] ==0 :
                bfs(i,j)
                cnt+=1
    if cnt != 0 :
        for i in range(N):
            for j in range(M):
                ripe(i,j)
                cnt = 0
        day += 1
        graph = copy.deepcopy(graph2)
    else: break


print(day)