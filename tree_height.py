import sys
import threading
import os

def compute_height(n, parents):
    tree = {}
    for node, parent in enumerate(parents):
        if parent ==-1:
            root = node
        else:
            if parent in tree:
                tree[parent].append(node)
            else:
                tree[parent] = [node]
    def height(node):
        if node not in tree:
            return 0
        return max(height(child) for child in tree[node])+1
    return height(root)

def main():
    mode = input() 
    if "F" in mode:
        filename = input()
        if not os.path.isfile(filename):
            print("Error: File does not exist.")
            return
        with open(filename, mode="r") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    elif "I" in mode:
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        print("Invalid mode.")
        return
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


