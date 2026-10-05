def subset_sum(nums, target):
    # Sort the numbers so pruning works
    nums = sorted(nums)

    found = []
    chosen = []

    def go(i, remaining):
        # Target reached
        if remaining == 0:
            found.append(chosen[:])
            return

        # No more numbers or next number is too large
        if i == len(nums) or nums[i] > remaining:
            return

        # Choose nums[i]
        chosen.append(nums[i])
        go(i + 1, remaining - nums[i])

        # Backtrack
        chosen.pop()

        # Skip nums[i]
        go(i + 1, remaining)

    # Start searching
    go(0, target)

    return found


# Test case 1
print(subset_sum([3, 34, 4, 12, 5, 2], 9))

# Test case 2
print(subset_sum([1, 2, 3], 7))