import heapq
n=5
k=2
h=[12,5,787,1,23]
print(h)
for i in range(n):
    h[i]*=(-1)


for i in range(k):
    heapq.heapify(h)
    p=heapq.heappop(h)
    if i==k-1:
        print((-1)*p)






