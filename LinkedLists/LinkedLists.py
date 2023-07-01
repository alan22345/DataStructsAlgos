import functools

class ListNode():
    def __init__(self, data=0, nextNode = None):
        self.data = data
        self.next = nextNode

def searchList(L,key):
    while L and L.data != key:
        L = L.next
    return L

def insertAfter(node, newNode):
    newNode.next = node.next
    node.next = newNode

def deleteAfter(node):
    node.next = node.next.next

def readThroughList(L):
    try: 
        print(L.data)
    except:
        return
    readThroughList(L.next)


L1 = ListNode(1,ListNode(3,ListNode(5,ListNode(7))))
L2 = ListNode(2,ListNode(4,ListNode(6,ListNode(8,ListNode(10)))))

# merge two LLs

def merge(L1,L2):
    dummyHead = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1, = L1 , L1.next   
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummyHead.next

dummy = merge(L1,L2)
# readThroughList(dummy)

# reverse a single sublist from start node to finish node

def reverseLL(L,start,finish):
    dummyHead = sublistHead = ListNode(0,L)

    for i in range(1, start):
        sublistHead = sublistHead.next
    sublistIter = sublistHead.next
    for i in range(finish-start):
        temp = sublistIter.next
        sublistIter.next, temp.next, sublistHead.next = temp.next, sublistHead.next,temp

    return dummyHead

reversedDummy = reverseLL(dummy, 3,8)
# readThroughList(reversedDummy)

# write a function to check if there is cyclicity within a LL,
# and return the start of the cycle if there is one

def hasCycle(head):
    def cycleLen(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            #find start of cycle
            cycleLenAdvancedIter = head
            for _ in range(cycleLen(slow)):
                cycleLenAdvancedIter = cycleLenAdvancedIter.next
            it = head
            # both iterators advance in tandem
            while it is not cycleLenAdvancedIter:
                it = it.next
                cycleLenAdvancedIter = cycleLenAdvancedIter.next
            return it
    return None

# testing for overlap

def length(L):
    length = 0
    while L:
        length += 1
        L = L.next
    return length

def overlappingLists(L1,L2):
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2,L1
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
    
    while L1 and L2 and L1 is not L2:
        L1,L2 = L1.next, L2.next
    return L1


# both lists can have a cycle if a node that appears first when traversing the lists exists 
# node may not be unique 
def overlappingListsWithCycles(L1,L2):
    root1, root2 = hasCycle(L1), hasCycle(L2)

    if not root1 and not root2:
        #neither list hasa cycle
        return overlappingLists(L1,L2)
    elif (root1 and not root2) or (not root1 and root2):
        return None
    
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break
    
    if temp is not root1:
        return None
    
    def distance(a,b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    #if L1 and L2 are in the same cycle, locate the overlapping node if they
    # overlap before cycle starts 
    stem1Len, stem2Len = distance(L1,root1), distance(L2,root2)
    if stem1Len > stem2Len:
        L2,L1 = L1,L2
        root1, root2 = root2, root1
    for _ in range(abs(stem1Len - stem2Len)):
        L2 = L2.next
    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1,L2 =L1.next, L2.next 
    return L1 if L1 is L2 else root1
    
# delete node from list 

def deleteNode(node):
    node.data = node.next.data
    node.next = node.next.next

# remove the kth last element from a list 
def removeKLast(L, k):
    dummyHead = ListNode(0,L)
    first = dummyHead.next
    for _ in range(k):
        first = first.next
    second = dummyHead
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    return dummyHead.next

# remove duplicates from a sorted linked list 

def removeDuplicates(L):
    it = L
    while it:
        nextDistinct = it.next
        while nextDistinct and nextDistinct.data == it.data:
            nextDistinct = nextDistinct.next
        it.next = nextDistinct
        it = nextDistinct
    return L

# cyclic right shift for singly linked list
# given list L and integer k, shift the list right by k

def cyclicRightShift(L,k):
    if not L:
        return L
    tail, n =L,1
    while tail.next:
        n += 1
        tail = tail.next
    
    k %= n
    if k == 0:
        return L
    
    tail.next = L
    stepsToNewHead, newTail = n-k, tail
    while stepsToNewHead:
        stepsToNewHead -= 1
        newTail = newTail.next
    newHead = newTail.next
    newTail.next = None 
    return newHead

# make all the odd nodes follow all the even nodes in linked list L

def evenOddMerge(L):
    if not L:
        return L
    evenDummyHead, oddDummyHead = ListNode(0), ListNode(0)
    tails, turn = [evenDummyHead, oddDummyHead], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1 # alternates between even and odd
    tails[1].next = None
    tails[0].next = oddDummyHead.next
    return evenDummyHead.next

# is linked list L palindromic?

def isLLPalindromic(L):
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    
    firstHalfIter, secondHalfIter = L, reverseLL(slow)
    while secondHalfIter and firstHalfIter:
        if secondHalfIter.data != firstHalfIter:
            return False
        secondHalfIter, firstHalfIter = firstHalfIter.next, firstHalfIter.next
    
    return True

# write a program that given a LL - L and a pivot p, returns a list 
# with all numbers less than p on the LHS and all all numbers larger than p
# on the RHS. Ordering of nodes on either side must remain unchanged

def pivotLL(L, p):
    lessHead = lessIter = ListNode()
    equalHead = equalIter = ListNode()
    greaterHead = greaterIter = ListNode()

    while L:
        if L.data < p:
            lessIter.next = L
            lessIter = lessIter.next
        elif L.data == p:
            equalIter.next = L
            equalIter = equalIter.next
        else:
            greaterIter.next = L
            greaterIter = greaterIter.next
        L = L.next

    greaterIter.next = None 
    equalIter.next = greaterHead.next
    lessIter.next = equalHead.next
    return lessHead.next

# add list based integers
# given two lists 1 -> 2 - > 9 and 2 -> 3 -> 5 result will be 532 + 921 = 1453 
# 3 -> 5 -> 4 -> 1

def addNumbers(L1, L2):
    placeIter = dummyHead = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + L2.data if L2 else 0
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        placeIter.next = ListNode(val%10)
        carry, placeIter = val//10,placeIter
    return dummyHead.next

