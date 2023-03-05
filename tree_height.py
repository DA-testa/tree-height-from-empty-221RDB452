import sys
import threading
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
    try:
        input_type = input("Enter input type (F for file, I for keyboard): ")
        if input_type == "F":
            filename = input("Enter filename: ")
            with open(filename, "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        elif input_type == "I":
            n = int(input())
            parents = list(map(int, input().split()))
        else:
            raise ValueError("Invalid input type. Please enter 'F' or 'I'.")
        print(compute_height(n, parents))
    except Exception as e:
        print("Error:", e)
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


