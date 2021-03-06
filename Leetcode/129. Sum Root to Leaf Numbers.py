"""
129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(N)
# Space complexity: O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # return self.morris(root)
        return self.dfs(root)
    
    # Time complexity: O(N)
    # Space complexity: O(H)
    def dfs(self, root):
        if not root: return 0
        total = self.helper(root, 0)
        return total
    
    def helper(self, root, curr):
        if root:
            curr = curr*10 + root.val
            if not root.left and not root.right:
                return curr
            
            left = self.helper(root.left, curr)
            right = self.helper(root.right,curr)
            
            if left and right:
                return left+right
            else:
                return left if left else right if right is not None else None
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def morris(self, root):
        total = curr = 0
        while root:
            if root.left:
                pre = root.left
                steps = 1
                while pre.right and pre.right is not root:
                    pre = pre.right
                    steps += 1
                    
                if not pre.right:
                    curr = curr*10 + root.val
                    pre.right = root
                    root = root.left
                else:
                    if not pre.left:
                        total += curr
                    for _ in range(steps):
                        curr //= 10
                    pre.right = None
                    root = root.right
            else:
                curr = curr*10 + root.val
                if not root.right:
                    total += curr
                root = root.right
        return total
