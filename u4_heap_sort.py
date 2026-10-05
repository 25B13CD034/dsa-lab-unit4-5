def heapify(a, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and a[left] > a[largest]:
        largest = left

    # Check right child
    if right < n and a[right] > a[largest]:
        largest = right

    # If largest is not the parent, swap
    if largest != i:
        a[i], a[largest] = a[largest], a[i]

        # Continue heapifying
        heapify(a, n, largest)


def build_max_heap(a):
    n = len(a)

    # Start from the last parent node
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)


def heap_sort(a):
    # Build max heap
    build_max_heap(a)

    print("Max-heap:", a)

    # Move largest element to the end
    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]

        # Heapify the remaining elements
        heapify(a, end, 0)

    return a


# Main program
data = [4, 10, 3, 5, 1, 8]

print("Input  :", data)
print("Sorted :", heap_sort(data[:]))