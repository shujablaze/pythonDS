class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def make_tree(self):
        data = int(input("Enter data or -1 for null: "))
        if data == -1:
            return None
        node = Node(data)

        print(f"Left child of {node.data}:")
        node.left = self.make_tree()
        print(f"Right child of {node.data}:")
        node.right = self.make_tree()

        self.root = node
        return node

    def in_order(self, node="root"):
        if node == "root":
            node = self.root
        if node.left is not None:
            self.in_order(node.left)
        print(f"{node.data} ", end="")
        if node.right is not None:
            self.in_order(node.right)

    def pre_order(self, node="root"):
        if node == "root":
            node = self.root
        print(f"{node.data} ", end="")
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)

    def post_order(self, node="root"):
        if node == "root":
            node = self.root
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        print(f"{node.data} ", end="")

    def get_height(self, node="root",cur_height=0):
        if node == "root":
            node = self.root
        if node.left is None and node.right is None:
            array.append(cur_height)
            return
        if node.left:
            self.get_height(node.left, cur_height+1)
        if node.right:
            self.get_height(node.right, cur_height+1)

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

array = 0

my_tree = Tree()
my_tree.make_tree()
array = my_tree.height()
print(array)


'''print("Inorder:", end="")
my_tree.in_order()
print("\nPreorder:", end="")
my_tree.pre_order()
print("\nPostorder:", end="")
my_tree.post_order()
'''