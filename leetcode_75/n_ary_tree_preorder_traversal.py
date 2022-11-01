'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.
'''

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> int:
        if not root:
            return []
        stack = [root]
        output = []
        
        while stack:
            top = stack.pop()
            output.append(top.val)
            stack.extend(reversed(top.children))
        
        return output
'''
class Solution:
    def preorder(self, root: 'Node') -> int:
        out = list()
        count = 0
        temp = list()
        while root:
            if count == 0:
                out.append(root.val)
                count += 1
            elif root.val == null:
                out.append(root.val)
                count += 1 
            else:
                temp.append(root.val)
        return [0,0]
'''
# Test Cases
s = Solution()
root = Node([1,None ,3,2,4,None ,5,6])
out = s.preorder(root)
print(out)
'''
s = Solution()
root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
out = s.preorder(root)
print(out)
'''