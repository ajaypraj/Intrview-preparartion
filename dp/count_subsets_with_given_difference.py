# Import numpy for creating and managing the DP table
import numpy as np

# Input array of numbers (can be treated like coin values or subset elements)
arr = [1, 1, 2, 3]

# Target difference between two subsets
diff = 1

# Number of elements in the array
n = len(arr)

# Transform the problem into a subset sum problem:
# We want to find the number of subsets with sum = (diff + total_sum) / 2
# This is based on the formula: S1 - S2 = diff and S1 + S2 = total_sum
# Solving gives: S1 = (diff + total_sum) / 2
s = int((diff + sum(arr)) / 2)

# Initialize a 2D DP table with dimensions (n+1) x (s+1)
# t[i][j] will store the number of subsets from the first 'i' elements that sum to 'j'
t = np.zeros((n+1, s+1))

# Print the initial DP table (optional)
print("Initial DP table:")
print(t)

# Base case initialization
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            # If no elements are available, we can't form any positive sum
            t[i][j] = 0
        if j == 0:
            # There is always one subset (empty set) that sums to 0
            t[i][j] = 1

# Fill the DP table using bottom-up approach
for i in range(1, n+1):
    for j in range(1, s+1):
        if arr[i-1] <= j:
            # Include the current element + exclude the current element
            t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
        else:
            # If current element is greater than sum, we can't include it
            t[i][j] = t[i-1][j]

# Print the final DP table (optional)
print("Final DP table:")
print(t)

# Final result: number of subsets with the required sum
print(f"Number of subsets with difference {diff} is {int(t[n][s])}")
