import heapq
h=[1,2,3,1,4,5,2,3,6]
l=len(h)
print(h)
for i in range(l):
    s=h[i:i+3]
    for j in range(3):
        s[j]*=(-1)
    heapq.heapify(s)
    print(heapq.heappop(s)*(-1)) 




