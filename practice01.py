# 백준 1937 욕심쟁이 판다
# 방문을 했던 좌표를 다시 방문할 수도 있다는 것임.
# 그러나 나 자신으로 돌아오는 것은 하면 안된다. 
# 자꾸 시간초과 나서 못 풀었다..ㅠㅠ 그래서 다른사람의 코드를 참조했다. 처음 심는 잔디가 이런 것이라 슬프다. 하지만 내 양분이 되리라..
# 두고두고 다시 와서 사고의 흐름을 체크하자

# visit라고 이름 짓지 말았어야함(어차피 방문여부체크하는 것이 아니므로)
# 어쨌든 visit 배열의 자기 자신의 칸에다 그 칸으로부터 방문할 수 있는 최대수를 저장해야함

import sys
T = int(input()) #Test case
sys.setrecursionlimit(10**6)

graph = [list(map(int, input().split())) for i in range(T)]
visit = [[0 for _ in range(T)] for _ in range(T)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if visit[x][y]: return visit[x][y]
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<T and -1<ny<T and graph[nx][ny] > graph[x][y]:
            visit[x][y] = max(visit[x][y], dfs(nx,ny)+1)
    return visit[x][y]
cnt = 0
for i in range(T):
    for j in range(T):
        cnt = max(dfs(i,j),cnt)

print(cnt)