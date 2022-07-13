# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in
# reverse order, and each of their nodes contains
# a single digit. Add the two numbers and return the sum
# as a linked list.

# You may assume the two numbers do not contain any leading
# zero, except the number 0 itself.

 # Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
from codecs import latin_1_decode
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.l2 = l2
        carry = 0
        dummy = ListNode(0, None)
        previous = dummy
        while (l1 or l2):
            sum, carry = self.sum(l1, l2, carry)
            current = ListNode(sum, None)
            l1, l2, current, previous = self.update_nodes(l1, l2, current, previous)
        if carry:
            current = ListNode(1, None)
            previous.next = current        
        return dummy.next

    def sum(self, l1, l2, carry):
        value1 = 0 if not l1 else l1.val
        value2 = 0 if not l2 else l2.val
        sum = value1 + value2 + carry
        carry = 0
        if sum >= 10:
            sum = sum % 10
            carry = 1
        return (sum, carry)

    def update_nodes(self, l1, l2, current, previous):       
        previous.next = current
        previous = current
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        return (l1, l2, current, previous)

    def create_linked_list(self, list):
        i = len(list) - 1
        tempNode = None
        while i >= 0:
            tempNode = ListNode(list[i], tempNode)
            i -= 1
        return tempNode
    
    def print_linked_list(self, head):
        while head:
            print(head.val, end =" ")
            head = head.next
        print("")

solution = Solution()
head1 = solution.create_linked_list([0])
print("First list: ", end = " ")
solution.print_linked_list(head1)
print("Second list:", end = " ")
head2 = solution.create_linked_list([0])
solution.print_linked_list(head2)

result = solution.addTwoNumbers(head1, head2)
print("Solution: ", end = " ")
solution.print_linked_list(result)