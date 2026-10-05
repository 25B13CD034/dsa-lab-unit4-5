def matrix_chain(dims):
    n = len(dims) - 1  # Number of matrices

    # Cost table
    cost = [[0] * n for _ in range(n)]

    # Split table
    split = [[0] * n for _ in range(n)]

    # length = chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            # Set initial cost to infinity
            cost[i][j] = float("inf")

            # Try every possible split
            for k in range(i, j):

                c = (
                    cost[i][k]
                    + cost[k + 1][j]
                    + dims[i] * dims[k + 1] * dims[j + 1]
                )

                # Keep the minimum cost
                if c < cost[i][j]:
                    cost[i][j] = c
                    split[i][j] = k

    return cost, split


def parens(split, i, j):
    # Only one matrix
    if i == j:
        return "A" + str(i + 1)

    # Get the best split position
    k = split[i][j]

    return (
        "("
        + parens(split, i, k)
        + " x "
        + parens(split, k + 1, j)
        + ")"
    )


# Main program
# A1 = 10x30
# A2 = 30x5
# A3 = 5x60
dims = [10, 30, 5, 60]

cost, split = matrix_chain(dims)

print("Minimum multiplications:", cost[0][-1])
print("Best order:", parens(split, 0, len(dims) - 2))