class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(node.data, end=" ")
            self.print_tree(node.right)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("In-order traversal of the binary tree:")
    tree.print_tree(tree.root)