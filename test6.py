N, M = map(int, input().split())
cakes = list(map(int, input().split()))

low = 0
high = max(cakes)
result=0


while(low<=high):
    middle = (low+high)//2
    total=0
    
    for x in cakes:
        if x>middle:
            total += x-middle
            
    if total >= M:
        result = middle
        low = middle+1
    else: 
        high = middle-1
        
print(result)
        