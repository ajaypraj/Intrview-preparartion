# Importing numpy for matrix operations
import numpy as np

# List of available coin denominations
coin = [1, 2, 3]

# Target sum we want to achieve using minimum number of coins
s = 5

# Number of coin types
n = len(coin)

# Define positive infinity to represent unreachable states
max_inf = float('inf')

# Initialize a 2D DP table with dimensions (n+1) x (s+1)
# t[i][j] will store the minimum number of coins needed to make sum 'j' using first 'i' coins
t = np.zeros((n+1, s+1))

# Fill the DP table with base conditions
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            # If no coins are available, we can't form any positive sum
            t[i][j] = max_inf - 1
        if i > 0:
            # If sum is 0, we need 0 coins regardless of coin types
            t[i][0] = 0

# Print the initial state of the DP table
print("Initial DP table after base case setup:")
print(t)

# Fill the second row of the table using only the first coin
for j in range(1, s+1):
    if j % coin[0] == 0:
        # If the sum is divisible by the coin value, use that many coins
        t[1][j] = j / coin[0]
    else:
        # Otherwise, mark it as unreachable
        t[1][j] = max_inf - 1

# Fill the rest of the DP table using bottom-up approach
for i in range(2, n+1):
    for j in range(1, s+1):
        if coin[i-1] <= j:
           
