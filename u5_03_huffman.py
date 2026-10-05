import heapq


def huffman_codes(freq):
    # Create a min-heap
    heap = [
        [weight, i, [[ch, ""]]]
        for i, (ch, weight) in enumerate(freq.items())
    ]

    heapq.heapify(heap)

    counter = len(heap)

    # Build Huffman tree
    while len(heap) > 1:
        # Take two nodes with the smallest weights
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        # Add 0 to codes in the first node
        for pair in lo[2:]:
            pair[1] = "0" + pair[1]

        # Add 1 to codes in the second node
        for pair in hi[2:]:
            pair[1] = "1" + pair[1]

        # Merge the two nodes
        heapq.heappush(
            heap,
            [lo[0] + hi[0], counter] + lo[2:] + hi[2:]
        )

        counter += 1

    # Return character -> Huffman code
    return {
        ch: code
        for ch, code in heap[0][2:]
    }


# Frequency table
freq = {
    "a": 45,
    "b": 13,
    "c": 12,
    "d": 16,
    "e": 9,
    "f": 5
}


# Generate Huffman codes
codes = huffman_codes(freq)


# Display codes
for ch in sorted(codes, key=lambda c: (len(codes[c]), c)):
    print(ch, freq[ch], codes[ch])


# Calculate Huffman encoded bits
bits = sum(
    freq[c] * len(codes[c])
    for c in freq
)


# Calculate fixed-length 3-bit encoding
fixed = sum(freq.values()) * 3


print("Huffman bits:", bits, "| fixed 3-bit bits:", fixed)