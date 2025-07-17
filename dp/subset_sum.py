
# Input array and target sum
import numpy as np
arr =[2,3,7,8,10]
n=len(arr)
sum = 11
t=np.zeros((n+1,sum+1),dtype=bool)
# t[n+1][sum+1]=[][]
for i in range(n+1):
    for j in range(sum+1):
        if i==0:
            t[i][j]=False
        if j==0:
            t[i][j]=True

for i in range(1,n+1):
    for j in range(1,sum+1):
        if arr[i-1]<=j:
            t[i][j]= (t[i-1][j-arr[i-1]]) or (t[i-1][j])
        elif arr[i-1] >j:
            t[i][j]=t[i-1][j]
print(f"Subset sum will exist {t[n][sum]}")
