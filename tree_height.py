import sys

def construct_tree(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            if parent in tree:
                tree[parent].append(node)
            else:
                tree[parent] = [node]
    return root, tree

def compute_height(root, tree):
    def height(node):
        if node not in tree:
            return 0
        return max(height(child) for child in tree[node]) + 1
    return height(root)

def main():
    mode = input()
    if mode == 'F':
        filename = input()
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    elif mode == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        print("Invalid mode.")
        return
    root, tree = construct_tree(n, parents)
    print(compute_height(root, tree))

sys.setrecursionlimit(10**7)  # max depth of recursion
main()

