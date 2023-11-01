# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def nodeSearch(name,root):
    if root != None:
        value = root.val
        if name.get(value) == None:
            name[value] = 1
        else:
            name[value] += 1
        nodeSearch(name,root.left)
        nodeSearch(name,root.right)
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        name = {}
        nodeSearch(name,root)
        occurence = 0
        for node in name:
            amount = name[node]
            if amount > occurence:
                occurence = amount
            
        arr = []
        for node in name:
            if name[node] == occurence:
                arr.append(node)
        return arr
       