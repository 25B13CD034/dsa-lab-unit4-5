def merge_sort(a):
    # Base case
    if len(a) <= 1:
        return a

    # Find middle
    mid = len(a) // 2

    # Divide the list into two halves
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def binary_search(a, target):
    low = 0
    high = len(a) - 1
    steps = 0

    while low <= high:
        steps += 1

        mid = (low + high) // 2

        if a[mid] == target:
            return mid, steps

        elif a[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, steps


# Main program
data = [38, 27, 43, 3, 9, 82, 10]

print("Original :", data)

sorted_data = merge_sort(data)

print("Sorted   :", sorted_data)

print("Search 43:", binary_search(sorted_data, 43))

print("Search 50:", binary_search(sorted_data, 50))