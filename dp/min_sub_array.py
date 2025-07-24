# Import numpy for creating and managing the DP table
import numpy as np

# Input array
arr = [1, 2, 7]

# Total sum of all elements
s = sum(arr)

# Number of elements in the array
n = len(arr)

# Initialize a 2D DP table with dimensions (n+1) x (s+1)
# t[i][j] will be True if a subset of the first 'i' elements has a sum equal to 'j'
t = np.zeros((n+1, s+1), dtype=bool)

# Base case initialization
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            # If no elements are available, we can't form any positive sum
            t[i][j] = False
        if j == 0:
            # A sum of 0 is always possible with an empty subset
            t[i][j] = True

# Fill the DP table using bottom-up approach
for i in range(1, n+1):
    for j in range(1, s+1):
        if arr[i-1] <= j:
            # Include or exclude the current element
            t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
        else:
            # If current element is greater than sum, we can't include it
            t[i][j] = t[i-1][j]

# Print the last row of the DP table which shows all achievable subset sums
print("Subset sums possible with all elements:")
print(t[n])

# Store the last row for easier access
x = t[n]

# Initialize minimum difference to infinity
m = float('inf')

# Iterate through the first half of the subset sums
# We're only interested in sums up to s//2 to minimize the difference
for i, x in enumerate(x[:int((s+1)/2)]):
    print(i, x)
    if x:
        # Update the minimum difference
        m = min(m, s - 2*i)

# Print the minimum subset sum difference
print(f"Minimum subset sum difference is: {m}")
