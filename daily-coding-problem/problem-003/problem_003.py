# This class was given by the problem statement.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # add a __repr__ to solve the problem
    def __repr__(self):
        return f"Node(val={self.val!r}, left={self.left!r}, right={self.right!r})"

def serialize(node):
    return repr(node)

def deserialize(s):
    return eval(s)

def serialize_beta(node):
    if node is None:
        return "None"
    return f"Node(val={node.val!r}, left={serialize_beta(node.left)}, right={serialize_beta(node.right)})"
