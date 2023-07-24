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

# does exist in sum in tree

def hasPathSum(tree, remaining_weight):
    if not tree:
        return False 
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    return (hasPathSum(tree.left, remaining_weight-tree.data)
            or hasPathSum(tree.right, remaining_weight-tree.data))

# inOrderTraversal

def inOrderTraversal(tree):
    s, result = [], []
    
    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    return result 

#pre order traversal

def preorderTraversal(tree):
    path, result = [tree], []
    while path:
        curr = path.pop()
        if curr: 
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result

# find the kth node in an inorder traversal 

def findKthNodeTree(tree, k):
    while tree:
        leftSize = tree.left.size if tree.left else 0
        if leftSize + 1 < k:
            k -= leftSize + 1
            tree = tree.right
        elif leftSize == k -1:
            return tree
        else:
            tree = tree.left 
    return None

# find the successor, the successor is the node that appears directly after the given node in an inorder traversal

def findSuccessor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node.parent.right is node:
        node = node.parent

    return node.parent

# reconstruct a tree from traversal data. inorder and preorder traversal data

def binaryTreeFromInorderPreorder(preorder, inorder):
    nodeToInorderId = {data: i for i, data in enumerate(inorder)}

    def binaryTreeFromPreorderInorderHelper(preorderStart, preorderEnd, inorderStart, inorderEnd):
        if preorderEnd <= preorderStart or inorderEnd <= inorderStart:
            return None
        
        rootInorderId = nodeToInorderId[preorder[preorderStart]]
        leftSubtreeeSize = rootInorderId - inorderStart
        return treeNode(
            preorder[preorderStart],
            binaryTreeFromPreorderInorderHelper(
                preorderStart + 1, preorderStart + 1 + leftSubtreeeSize,
                inorderStart, rootInorderId
            ),
            binaryTreeFromPreorderInorderHelper(
                preorderStart + 1 + leftSubtreeeSize,
                preorderEnd, rootInorderId + 1, inorderEnd)
            )
    return binaryTreeFromPreorderInorderHelper(0, len(preorder), 0, len(inorder))

# reconstruct a binary tree from a preorder traversal with null if a child is empty
def reconstructFromPreorder(preorder):
    def reconstructPreorderHelper(preorderIter):
        subtreeKey = next(preorderIter)
        if subtreeKey is None:
            return None
        leftSubtree = reconstructPreorderHelper(preorderIter)
        rightSubtree = reconstructPreorderHelper(preorderIter)
        return treeNode(subtreeKey, leftSubtree, rightSubtree)
    return reconstructPreorderHelper(iter(preorder))

# given a binary tree compute linked list from the leaves of the binary tree

def createListOfLeaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    return createListOfLeaves(tree.left) + createListOfLeaves(tree.right)

#compute the exterior of a binary tree

def exteriorBinaryTree(tree):
    def isLeaf(node):
        return not node.left and not node.right
    
    def leftBoundaryAndLeaves(subtree, isBoundary):
        if not subtree:
            return []
        return (([subtree] if isBoundary
            or isLeaf(subtree) else []) + leftBoundaryAndLeaves(
                subtree.left,isBoundary) + leftBoundaryAndLeaves(
                    subtree.right, isBoundary and not subtree.left
                ))
    def rightBoundaryAndLeaves(subtree, isBoundary):
        if not subtree:
            return []
        return (rightBoundaryAndLeaves(subtree.left, isBoundary and not subtree.right) +
        rightBoundaryAndLeaves(subtree.right, isBoundary) + 
        ([subtree] if isBoundary or isLeaf(subtree) else []))
    
    return ([tree] + leftBoundaryAndLeaves(tree.left, isBoundary=True) + 
        rightBoundaryAndLeaves(tree.right, isBoundary=True)
        if tree else [])

def computeRightSiblingTree(tree):
    def populateChildrenNextField(startNode):
        while startNode and startNode.left:
            
            startNode.left.next = startNode.right
            startNode.right.next = startNode.next and startNode.next.left
            startNode = startNode.next
        
    while tree and tree.left:
        populateChildrenNextField(tree)
        tree = tree.left
        

