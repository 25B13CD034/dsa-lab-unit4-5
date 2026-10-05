def find(parent, x):
    # Find the root of x
    while parent[x] != x:
        # Path compression
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def kruskal(n, edges):
    # Initially, every node is its own parent
    parent = list(range(n))

    mst = []
    total = 0

    # Sort edges by weight
    for w, u, v in sorted(edges):

        # Find roots of both vertices
        ru = find(parent, u)
        rv = find(parent, v)

        # If they belong to different groups
        if ru != rv:
            # Join the groups
            parent[ru] = rv

            # Add edge to MST
            mst.append((u, v, w))
            total += w

            print(f"Add edge {u}-{v} (w={w})")

        else:
            # Edge creates a cycle
            print(f"Skip edge {u}-{v} (w={w}) - forms a cycle")

    return mst, total


# Edges are in the format: (weight, u, v)
edges = [
    (4, 0, 1),
    (8, 0, 2),
    (2, 1, 2),
    (6, 1, 3),
    (3, 2, 3),
    (5, 2, 4),
    (7, 3, 4)
]


# Find the Minimum Spanning Tree
mst, total = kruskal(5, edges)

print("MST weight:", total)