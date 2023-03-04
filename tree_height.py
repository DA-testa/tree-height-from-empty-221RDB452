# python3
import sys
import threading
def compute_height(n, parents):
    heights = [0] * n
    for i in range(n):
        node = i
        height = 0
        while node != -1:
            if heights[node] != 0:
                height += heights[node]
                break
            height += 1
            node = parents[node]
        heights[i] = height
    return max(heights)
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


