# Import numpy for creating and managing the DP table
import numpy as np

# List of coin denominations
arr = [1, 2, 3]

# Target sum we want to form
s = 5

# Objective: Find how many ways we can form the sum 's' using coins of 1, 2, and 3 rupees

# Number of coin types
n = len(arr)

# Initialize a 2D DP table with dimensions (n+1) x (s+1)
# t[i][j] will store the number of ways to make sum 'j' using the first 'i' coins
t = np.zeros((n+1, s+1), dtype=int)

# Base case initialization
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            # If no coins are available, we can't form any positive sum
            t[i][j] = 0
        if j == 0:
            # There is exactly one way to make sum 0 — by choosing no coins
            t[i][j] = 1

# Fill the DP table using bottom-up approach
for i in range(1, n+1):
    for j in range(1, s+1):
        if arr[i-1] <= j:
            # Include the coin: number of ways to make (j - coin value) with current coins
            # Exclude the coin: number of ways to make j without using current coin
            t[i][j] = t[i][j - arr[i-1]] + t[i-1][j]
        else:
            # If coin value is greater than current sum, we can't include it
            t[i][j] = t[i-1][j]

# Print the entire DP table (optional, for debugging or understanding)
print("DP Table:")
print(t)

# Final result: number of ways to make sum 's' using all available coins
print(f"Number of ways to make sum {s} is {t[n][s]}")
