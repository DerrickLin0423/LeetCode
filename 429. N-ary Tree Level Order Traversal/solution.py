# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
            

def buildTree(nodes: 'list') -> Node:
    originalRoot = Node(nodes[0])
    root = originalRoot
    nextRoot = [root]
    for val in nodes[1:]:
        if val == None:
            # change root to something else
            root = nextRoot[0]
            nextRoot = nextRoot[1:]
            continue
        if root.children == None:
            root.children = []
        child = Node(val)
        root.children.append(child)
        nextRoot.append(child)
    return originalRoot


class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        result = []
        currentLevel = [root]
        
        while True:
            levelVal = []
            nextLevel = []

            for node in currentLevel:
                if node != None:
                    levelVal.append(node.val)
                    if node.children != None:
                        nextLevel.extend(node.children)

            if len(levelVal) > 0:
                result.append(levelVal)
            currentLevel = nextLevel

            if len(nextLevel) == 0:
                return result
            
            