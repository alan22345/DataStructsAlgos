import collections

def treeNode():
    def __init__(self, data = None, left= None, right = None):
        self.data = data
        self.left = left
        self.right = right

def isBalancedBinaryTree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight',('balanced','height'))

    def isBalanced(tree):
        
        leftResult = isBalanced(tree.left)
        if not leftResult.balanced:
            return BalancedStatusWithHeight(False,0)
        
        rightResult = isBalanced(tree.right)
        if not rightResult.balanced:
            return BalancedStatusWithHeight(False,0)

        is_balanced = abs(leftResult.height - rightResult.height) <= 1
        height = max(leftResult.height,rightResult.height) + 1
        
        return BalancedStatusWithHeight(is_balanced,height)
    return isBalanced(tree).balanced
    
