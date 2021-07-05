class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data, cur_node="None"):
        new_node = Node(data)
        if cur_node == "None":
            cur_node = self.root

        if cur_node.data < data and cur_node.right is None:
            cur_node.right = new_node
            return
        if cur_node.data > data and cur_node.left is None:
            cur_node.left = new_node
            return

        if cur_node.data < data:
            self.insert(data, cur_node.right)
        else:
            self.insert(data, cur_node.left)

    def in_order(self, node="root"):
        if node == "root":
            node = self.root
        if node.left is not None:
            self.in_order(node.left)
        print(f"{node.data} ", end="")
        if node.right is not None:
            self.in_order(node.right)

    def height(self, node="root"):
        if node == "root":
            node = self.root

        if node is None:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if left > right:
            return left+1
        else:
            return right+1


bst = Bst(23)

array = [35, 80, 2, 13, 56, 11, 60, 71]

for num in array:
    bst.insert(num)

bst.in_order()
print("\nHeight of the given BST is ", end="")
print(bst.height())

