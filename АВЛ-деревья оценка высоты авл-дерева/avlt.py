class Node:
    def __init__(self, d):
        self.key = d
        self.height = 1
        self.left = None
        self.right = None


def height(node:Node)->int:
    return 0 if node is None else node.height


def right_rotate(y:Node)->Node:
    x = y.left
    y.left = x.right
    x.right = y
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def big_right_rotate(x:Node)->Node:
    return right_rotate(left_rotate(x.left))

def big_left_rotate(x:Node)->Node:
    return left_rotate(right_rotate(x.right))

def left_rotate(x:Node)->Node:
    y = x.right
    x.right = y.left
    y.left = x
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y


def get_balance(node:Node)->int:
    return 0 if node is None else height(node.left) - height(node.right)


def insert(key:int, node:Node=None)->Node:
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(key, node.left)
    elif key > node.key:
        node.right = insert(key, node.right)
    else:
        return node

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return right_rotate(node)
    if balance < -1 and key > node.right.key:
        return left_rotate(node)
    if balance > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    return node


def delete(key:int, node:Node=None)->Node:
    if not node:
        return node
    if key < node.key:
        node.left = delete(key, node.left)
    elif key > node.key:
        node.right = delete(key, node.right)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp = get_min_value_node(node.right)
        node.key = temp.key
        node.right = delete(temp.key, node.right)

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    return node

def get_min_value_node(node:Node)->str:
    current = node
    while current.left is not None:
        current = current.left
    return current


def find_value(key:int, node:Node)->bool:
    if key == node.key:
        return True
    if node.height == 1:
        return key == node.key
    return find_value(key, node.left) if node.key > key else find_value(key, node.right)


def get_node_info(node:Node)->str:
    return f"k:{node.key}, h:{node.height}"


def print_tree_dop(node:Node)->str:
    if node.height != 1:
        left = ("(" + print_tree_dop(node.left) + ")<=" if not node.left is None else "") + "("
        right = ")" + ("=>(" + print_tree_dop(node.right) + ")" if not node.right is None else "")
        return left + get_node_info(node) + right
    else:
        return get_node_info(node)


tree = insert(5)
tree = insert(4, tree)
tree = insert(6, tree)
tree = insert(7, tree)
tree = insert(8, tree)
print(print_tree_dop(tree))
tree = insert(9, tree)
print(print_tree_dop(tree))
tree = delete(7, tree)
print(print_tree_dop(tree))
print(find_value(7, tree))
print(find_value(5, tree))