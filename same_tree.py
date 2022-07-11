# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.

# Two binary trees are considered the same if they are
# structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

from sre_constants import SUCCESS
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current_p = [p]
        lower_p = []
        current_q = [q]
        lower_q = []
        while(len(current_p) > 0):
            for i in range(len(current_p)):
                if not self.same(current_p[i], current_q[i]):
                    return False
                if current_p[i]:
                    lower_p.append(current_p[i].left)
                    lower_p.append(current_p[i].right)
                    lower_q.append(current_q[i].left)
                    lower_q.append(current_q[i].right)
            current_p = lower_p
            current_q = lower_q
            lower_p = []
            lower_q = []
        return True

    def same(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            #print(f"p.val: {p.val} q.val: {q.val}")
            return True
        else:
            return False

    def print_tree(self, head):
        current_level = [head]
        lower_level = []
        while(True):
            for e in current_level:
                print(f"{e.val}", end = " ")
                if e.left:
                    lower_level.append(e.left)
                if e.right:
                    lower_level.append(e.right)
            if not lower_level:
                return 1
            current_level = lower_level
            lower_level = []

def main():
    solution = Solution()
    head = TreeNode(1)
    child2 = TreeNode(2)
    child3 = TreeNode(3)
    gchild4 = TreeNode(4)
    gchild5 = TreeNode(5)
    gchild7 = TreeNode(7)
    head.left = child2
    head.right = child3
    child2.left = gchild4
    child2.right = gchild5
    child3.right = gchild7
    #print(solution.isSameTree(head, head))
    head2 = TreeNode(1)
    child2_2 = TreeNode(2)
    child2_3 = TreeNode(3)
    gchild2_4 = TreeNode(4)
    gchild2_5 = TreeNode(6)
    gchild2_7 = TreeNode(7)
    head2.left = child2_2
    head2.right = child2_3
    child2_2.left = gchild2_4
    child2_2.right = gchild2_5
    child2_3.right = gchild2_7
    print(solution.isSameTree(head, head2))

if __name__ == "__main__":
    main()

# Success
# Runtime: 31 ms, faster than 93.14% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 29.37% of Python3 online submissions for Same Tree.
    