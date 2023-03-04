import sys
import threading

def compute_height(n, parents):
    """
    Computes the height of a tree given its parent array representation.

    Args:
        n (int): The number of nodes in the tree.
        parents (list): An array of integers representing the parent of each node.

    Returns:
        The height of the tree.
    """
    # Create the tree
    tree = {}
    for node, parent in enumerate(parents):
        if parent == -1:
            root = node
        else:
            if parent in tree:
                tree[parent].append(node)
            else:
                tree[parent] = [node]

    def height(node):
        if node not in tree:
            return 0
        return max(height(child) for child in tree[node]) + 1
    
    return height(root)

def main():
    """
    Prompts the user to enter input type (file or keyboard) and reads input accordingly.
    Then computes and prints the height of the tree.
    """
    try:
        input_type = input("Enter input type (F for file, I for keyboard): ")
        if input_type == "F":
            # Read input from file
            filename = input("Enter filename: ")
            with open(filename, "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        elif input_type == "I":
            # Read input from keyboard
            n = int(input())
            parents = list(map(int, input().split()))
        else:
            raise ValueError("Invalid input type. Please enter 'F' or 'I'.")

        # Compute and output tree height
        print(compute_height(n, parents))

    except Exception as e:
        print("Error:", e)


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


