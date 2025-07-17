# write a code for equal subset sum 
# return T/F if two subset exists if there sum is equal
arr = [1,5,11,5]
n=len(arr)
def is_sum_possible(n,sum):
    t= np.zeros((n+1,sum+1),dtype=bool)
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            elif arr[i-1] > sum :
                t[i][j]=t[i-1][j]
    return t[n][sum]
import numpy as np
sum =0
for i in range(len(arr)):
    sum +=arr[i]
if sum %2 !=0:
    print("Two eqaul sum is not possible")
else:
    new_sum = int(sum/2)
    val = is_sum_possible(n, new_sum)
    print(f"Two equal sum is possible {val}")
