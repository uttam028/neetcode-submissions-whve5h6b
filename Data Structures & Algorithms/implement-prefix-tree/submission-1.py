class Node:
    def __init__(self, val:str|None=None):
        self.val = val
        self.children = {}
        self.terminating = False
    def addChild(self, node: 'Node'):
        self.children[node.val] = node

class PrefixTree:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if(char not in node.children.keys()):
                temp = Node(char)
                node.addChild(temp)
                node = temp
            else:
                node = node.children[char]
        node.terminating = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if(char not in node.children.keys()):
                return False
            else:
                node = node.children[char]
        if(node.terminating):
            return True
        return False 
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if(char not in node.children.keys()):
                return False
            else:
                node = node.children[char]
        return True
        
        