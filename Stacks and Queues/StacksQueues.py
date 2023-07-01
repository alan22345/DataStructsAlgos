"""
Stacks are last in first out for inserts and deletes
Queues are first in first out
Stacks only support pushes and pops
"""
import collections

# implement a max() function for a stack class

class Stack:
    ElementWithCachedMax = collections.namedtuple('elementWithCachedMax', ('element','max'))

    def __init__(self):
        self._elementWithCachedMax =[]
    
    def empty(self):
        return len(self._elementWithCachedMax) == 0
    
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._elementWithCachedMax[-1].max
    
    def pop(self):
        if self.empty():
            raise IndexError('empty')
        return self._elementWithCachedMax.pop().element
    
    def push(self, x):
        self._elementWithCachedMax.append(
            self.ElementWithCachedMax(x,x if self.empty() else max(x, self.max())))

# evaluate a reverse polish notation, google it

def evalRPN(expr):
    intermediateResults = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y,x: x + y, '-': lambda y, x:x -y, "*": lambda y,x: x*y,
        '/': lambda y,x: int(x/y)
    }
    for token in expr.split(DELIMITER):
        if token in OPERATORS:
            intermediateResults.append(OPERATORS[token](
                intermediateResults.pop(), intermediateResults.pop()
            ))
        else:
            intermediateResults.append(int(token))
    return intermediateResults[-1]

# test if all brackets in a string add up

def evalBrackets(s):
    remainingChars, lookup = [], {'(':')','{':'}','[':']'}
    for c in s:
        if c in lookup:
            remainingChars.append(c)
        elif not remainingChars or lookup[remainingChars.pop()] != c:
            return False 
    return not remainingChars

# take a pathname and return the shortest equivalent path
def equivalentPath(path):
    pathNames = []
    if path[0] == '/':
        pathNames.append('/')
    
    for token in (token for token in path.split('/') if token not in ['.','']):
        if token == '..':
            if not pathNames or pathNames[-1] == '..':
                pathNames.append(token)
            else:
                if pathNames[-1] == '/':
                    raise ValueError('Path error')
                pathNames.pop()
        else:
            pathNames.append(token)
    result = '/'.join(pathNames)
    return result[result.startswith('//'):]
