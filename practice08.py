#bfs만 공부해왔다보니까 bfs문제도 bfs 방식으로 풀려했다
#먼저 0으로 이루어진 섬의개수를 구하고 이것이 0이 되면 끝나는 함수를구현함
#day가 지날수록 토마토가 익는 ripe함수를 써서 1과 인접한 위치에 1을 부여했다.
#그러나 bfs로 풀면 쉬운것이었음.

import sys
from collections import deque
import copy

M,N = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().rstrip().split()))

graph2 = copy.deepcopy(graph)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(visit,x,y):
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
                if graph[nx][ny]==0:
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        queue.append((nx,ny))

def ripe(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0 <= ny < M :
            if graph2[x][y]==1 and graph2[nx][ny] ==0:
                graph[nx][ny] = 1

cnt = 0
day = 0

while True:
    cnt = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and graph[i][j] ==0 :
                bfs(visit,i,j)
                cnt+=1
    if cnt != 0 :
        for a in range(N):
            for b in range(M):
                ripe(a,b)
        day += 1
    else: break

print(day)