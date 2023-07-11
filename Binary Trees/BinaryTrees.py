import collections

class treeNode():
    def __init__(self, data=None, left= None, right = None):
        self.data = data
        self.left = left
        self.right = right
    



# a balanced binary tree is one where the subtrees height difference is at most 1

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
    
# a symmetric binary tree has the same node values as well as being structuraly
# symmetrical

def isSymmetricBinaryTree(tree):
    def checkSymmetry(subTreeA,subTreeB):
        if subTreeA and subTreeB:
            return (subTreeA.data == subTreeB.data
                and checkSymmetry(subTreeA.left, subTreeB.right)
                and checkSymmetry(subTreeA.right,subTreeB.left)) # checking the symmetry of the RHS and LHS of tree recursively 
        return False
    return checkSymmetry(tree.left,tree.right)

# compute the lowest common ancestor in a binary tree
# the LCA is the node furthest from the root that is a parent of both nodes

def findLCA(tree,nodeA,nodeB):
    status = collections.namedtuple('Status', ('numTargetNodes','ancestor'))

    # returns an object consisting of an int and a node, the int field is 0,
    # 1 or 2 depending on how many of {nodeA,nodeB} are present in the tree. If 
    # both are present in tree, when ancestor is assigned to a non null value 
    # it is the LCA

    def LCAHelper(tree, nodeA, nodeB):
        if not tree:
            return status(0, None)

        leftResult = LCAHelper(tree.left, nodeA, nodeB)
        if leftResult.numTargetNodes == 2:
            #found both nodes in left subtree
            return leftResult
        
        rightResult = LCAHelper(tree.right, nodeA, nodeB)
        if rightResult.numTargetNodes == 2:
            # found both nodes in right subtree
            return rightResult
        
        numTargetNodes = (
            leftResult.numTargetNodes + rightResult.numTargetNodes + int(
                tree is nodeA) + int(tree is nodeB))
        
        return status(numTargetNodes,tree if numTargetNodes == 2 else None)
    
    return LCAHelper(tree,nodeA,nodeB).ancestor

# compute LCA when nodes have parent pointers 

def findLCA2(nodeA,nodeB):
    def findDepth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent 
        return depth
    
    depthA, depthB = findDepth(nodeA), findDepth(nodeB)

    if depthA > depthB:
        nodeA, nodeB = nodeB, nodeA

    depthDiff = abs(depthA - depthB)
    while depthDiff:
        nodeA = nodeA.parent
        depthDiff -= 1
    
    while nodeA is not nodeB:
        nodeA, nodeB = nodeA.parent, nodeB.parent
    
    return nodeA

# a binary tree where each node is a 1 or a 0, find the sum of the root to leaf paths in the tree

def sumRootToLeaf(tree, partialPathSum = 0):
    if not tree:
        return 0
    
    partialPathSum = partialPathSum * 2 + tree.data
    if not tree.left and not tree.right: #leaf
        return partialPathSum
    return (sumRootToLeaf(tree.left,partialPathSum) + sumRootToLeaf(tree.right,partialPathSum))

# layer_2_rightleft = treeNode(0,treeNode(1),treeNode(1))
# layer_2_rightright = treeNode(0,treeNode(0),treeNode(1))
# layer_2_leftright = treeNode(1,treeNode(1))
# layer_2_leftleft = treeNode(0,treeNode(1,treeNode(0)))
# layer_1_left, layer_1_right = treeNode(1,layer_2_leftleft,layer_2_rightright), treeNode(0,layer_2_leftright,layer_2_rightleft)
# root = treeNode(1,layer_1_left,layer_1_right)

# sumRootToLeaf(root)

