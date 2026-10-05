def solve_queens(n):
    solutions = []

    # cols[r] = column of the queen in row r
    cols = []

    def safe(row, col):
        # Check all previously placed queens
        for r in range(row):
            c = cols[r]

            # Same column or same diagonal
            if c == col or abs(c - col) == abs(r - row):
                return False

        return True

    def place(row):
        # All queens have been placed
        if row == n:
            solutions.append(cols[:])
            return

        # Try every column
        for col in range(n):
            if safe(row, col):
                cols.append(col)

                # Move to the next row
                place(row + 1)

                # Backtrack
                cols.pop()

    # Start from row 0
    place(0)

    return solutions


# Solve 4-Queens
sols = solve_queens(4)

print("4-Queens solutions:", len(sols))

# Display all 4-Queens solutions
for s in sols:
    print(s)

    for r in range(4):
        print(
            " ".join(
                "Q" if c == s[r] else "."
                for c in range(4)
            )
        )

    print()


# Number of solutions for 6-Queens
print("6-Queens solutions:", len(solve_queens(6)))

# Number of solutions for 8-Queens
print("8-Queens solutions:", len(solve_queens(8)))