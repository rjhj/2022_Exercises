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

    def listToLL(self, list):
        tmpNode = ListNode(list[-1], None)
        for i in range(len(list)-2, 0, -1):
            tmpNode = ListNode(list[i], tmpNode)
        firstNode = ListNode(list[0], tmpNode)
        return firstNode

    def firstNodeToList(self, node):
        returnList = []
        while(node != None):
            returnList.append(node.val)
            node = node.next
        return returnList

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:          
        # Checking if both or one of the lists are empty
        if not list1 and not list2:
            return list2
        if not list1 or not list2:
            return list1 if not list2 else list2
        #Finding head
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        currentObject = head
        while True:
            #Checking if one of the lists is none. Both cannot be because of earlier check.
            if not list1 or not list2:
                currentObject.next = list1 if not list2 else list2
                return head
            if list1.val <= list2.val:
                currentObject.next = list1
                currentObject = list1
                list1 = list1.next
            else:
                currentObject.next = list2
                currentObject = list2
                list2 = list2.next


solver = Solution()

dummy = cur = ListNode()
cur.val = 3
print(dummy.val)

#Test cases
listOnes = [[1, 2, 4], [4]]
listTwos = [[1, 3, 4], [3]]
expectedOutput = [[1, 1, 2, 3, 4, 4], [3,4]]

#Tests
i = 0
while i < len(listOnes):
    firstHead = solver.listToLL(listOnes[i])
    secondHead = solver.listToLL(listTwos[i])
    #result = solver.mergeTwoLists(firstHead, secondHead)
    result = solver.mergeTwoLists(ListNode(4, None), ListNode(3, None))
    print(f"List1: {listOnes[i]}, List2: {listTwos[i]}")
    print(f"Expected: {expectedOutput[i]}, Result: {solver.firstNodeToList(result)}")
    i += 1

# Success
# Runtime: 41 ms, faster than 87.29% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 78.87% of Python3 online submissions for Merge Two Sorted Lists.