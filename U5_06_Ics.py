def lcs(a, b):
    m = len(a)
    n = len(b)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Walk backwards to find the actual LCS
    i = m
    j = n
    out = []

    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse the result
    return dp, "".join(reversed(out))


# Main program
a = "ABCBDAB"
b = "BDCABA"

dp, seq = lcs(a, b)

# Print DP table
for row in dp:
    print(row)

print("LCS length:", dp[-1][-1])
print("LCS       :", seq)