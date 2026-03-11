class CircularQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

def isValidPos(x,y):
    if x<0 or y<0 or x>=M or y>=N:    #미로 밖이면 갈 수 없음
        return False

    return graph[y][x]==1 or (x, y) == (M-1, N-1)   #괴물이 없는 부분(1)이거나 마지막 칸이면 갈 수 있음
        

        
def BFS():
    que = CircularQueue() #큐 객체 생성
    que.enqueue((0,0)) #처음 위치 큐에 넣기
    
    while not que.isEmpty():
        x,y=que.dequeue() #큐의 front 빼서 x,y에 넣어주기

        if (x,y) == (M-1,N-1):
            return graph[y][x]
            
        if isValidPos(x, y - 1):
            graph[y - 1][x] = graph[y][x] + 1 #시작점에서 그 칸까지의 거리를 저장
            que.enqueue((x, y - 1))

        if isValidPos(x, y + 1):
            graph[y + 1][x] = graph[y][x] + 1
            que.enqueue((x, y + 1))

        if isValidPos(x - 1, y):
            graph[y][x - 1] = graph[y][x] + 1
            que.enqueue((x - 1, y))

        if isValidPos(x + 1, y):
            graph[y][x + 1] = graph[y][x] + 1
            que.enqueue((x + 1, y))

    return False


    
    
        
# 입력 받기
N,M = map(int,input().split())

#지도 입력 받기
graph=[]
for _ in range(N):
    graph.append(list(map(int, input().strip())))
    
print(BFS())