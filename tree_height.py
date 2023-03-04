import sys
import threading
def compute_height(n, parents):
    # Create the tree
    tree = {}
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            parent = parents[i]
            if parent in tree:
                tree[parent].append(i)
            else:
                tree[parent] = [i]
    def height(node):
        if node not in tree:
            return 0
        return max(height(child) for child in tree[node]) + 1
    
    return height(root)
def main():
    
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

