# python3
import sys
import threading

def compute_height(n, parents):
    tree={}
    for i in range(n):
        tree[i]=[]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent==-1:
            root=i
        else:
            tree[parent].append(i)
    def height(node):
        if not tree[node]:
            return 1
        else:
            return max(height(child) for child in tree[node])+1
    return height(root)

def main():
    try:
        n = int(input("Enter the number of nodes in the tree: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    parents = list(map(int,input("Enter the parent of each node separated by spaces: ").split()))
    print(compute_height(n,parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

