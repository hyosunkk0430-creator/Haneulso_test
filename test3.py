class Stack:
    def __init__(self):
        self.top = []
        
    def isEmpty(self):return len(self.top) == 0
    

    def push(self,item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)



# 가로 세로 입력받기 N:세로 M:가로
N,M=map(int,input().split())

#얼음틀 입력받기
graph=[]
for _ in range(N):
    graph.append(list(map(int, input().strip())))
    

count = 0

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        # 아직 방문 안한 0이면 DFS 시작
        if graph[i][j] == 0:
            stack = [(i, j)]
            graph[i][j] = 1  # 방문 처리

            while stack:
                x, y = stack.pop()

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 범위 체크
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            stack.append((nx, ny))
                            graph[nx][ny] = 1  # 방문 처리

            count += 1

print(count)