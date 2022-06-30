# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return []


node2 = ListNode(2, None)
node1 = ListNode(1, node2)

solver = Solution()

print(f"Node1: {node1.val} Node2: {node1.next.val}")

#Test cases
listOnes = [[1, 2, 4]]
listTwos = [[1, 3, 4]]
expectedOutput = [[1, 1, 2, 3, 4, 4]]

#Tests
i = 0
while i < len(listOnes):
    print(f"List1: {listOnes[i]}, List2: {listTwos[i]}")
    print(f"Expected: {expectedOutput[i]}, Result: {solver.mergeTwoLists(listOnes[i], listTwos[i])}")
    i += 1