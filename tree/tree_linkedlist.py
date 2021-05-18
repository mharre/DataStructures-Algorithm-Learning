
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

tree = TreeNode('Drinks') #data = value of root node
left_child = TreeNode('Hot')
right_child = TreeNode('Cold')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')

left_child.left_child = tea
left_child.right_child = coffee

tree.left_child = left_child
tree.right_child = right_child


def preorder_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


def inorder_traversal(root_node):
    if not root_node:
        return
    else:
        inorder_traversal(root_node.left_child)
        print(root_node.data)
        inorder_traversal(root_node.right_child)


def postorder_traversal(root_node):
    if not root_node:
        return
    else:
        postorder_traversal(root_node.left_child)
        postorder_traversal(root_node.right_child)
        print(root_node.data)


def levelorder_traversal(root_node):
    if not root_node:
        return
    else:
        queue = queue.Queue()
        queue.enqueue(root_node)
        while not(queue.is_empty()): #if not empty
            root = queue.dequeue()
            print(root.value.data)
            if (root.value.left_child is not None):
                queue.enqueue(root.value.left_child)
            if (root.value.right_child is not None):
                queue.enqueue(root.value.right_child)
            


# preorder_traversal(tree)
# inorder_traversal(tree)
# postorder_traversal(tree)
# levelorder_traversal(tree) #must import queue to use 