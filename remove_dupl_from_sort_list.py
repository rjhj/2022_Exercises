# Given the head of a sorted linked list, delete all
# duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def createList(self, l):
        head = None
        for e in l:
            if head:
                current = ListNode(e)
                previous.next = current
                previous = current
            else:
                head = ListNode(e)
                previous = head
        return head

    def printList(self, head):
        while(head):
            print(head.val)
            head = head.next
            
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous = head
        current = previous.next
        while(current):
            if previous.val == current.val:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return head

#Testlist
l = []
solution = Solution()
head = solution.createList(l)
#solution.printList(head)
new_head = solution.deleteDuplicates(head)
solution.printList(new_head)

# Success
# Runtime: 64 ms, faster than 52.37% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.9 MB, less than 70.63% of Python3 online submissions for Remove Duplicates from Sorted List.