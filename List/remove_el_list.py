ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n=len(ar)
m=len(ar)
for i in range(0,n):
    for j in range(m):
        if(ar[j]==10):
            ar.remove(ar[j])
            m=len(ar)-1
            break
print(ar)
