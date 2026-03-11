
def selection_sort():
    N, K = map(int, input().split()) #원소 개수,최대 연산 횟수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(K):
        least = i
        biggest = i
        for k in range(N):     #최솟값 찾기 반복
            if (A[k]<A[least]):
                least = k
        for j in range(N):   #최댓값 찾기 반복           
            if (B[j]>B[biggest]):
                biggest=j
                    
        A[least],B[biggest] = B[biggest], A[least]   #A의 최솟값과 B의 최댓값을 교체
    print(sum(A))
            
    
            
            
selection_sort()