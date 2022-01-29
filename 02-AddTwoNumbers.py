"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      # input: l1: [2,4,3], l2: [5,6,4]
      # output: [7,0,8]
      # explanation: 342 + 465 = 807.

        # initialize the result list
        result = ListNode()
        # initialize the current node
        current = result
        # initialize the carry
        carry = 0
        
        # loop through the two lists
        while l1 or l2:
            # initialize the sum
            sum = carry
            # if l1 is not None, add the value to the sum
            if l1:
                sum += l1.val
                l1 = l1.next
            # if l2 is not None, add the value to the sum
            if l2:
                sum += l2.val
                l2 = l2.next
            # set the carry to the remainder of the sum divided by 10
            carry = sum // 10
            # set the current node's value to the remainder of the sum divided by 10
            current.val = sum % 10
            # if l1 or l2 is not None, create a new node and set the current node's next to the new node
            if l1 or l2:
                current.next = ListNode()
                current = current.next
        # if the carry is not 0, create a new node and set the current node's next to the new node
        if carry:
            current.next = ListNode(carry)
        # return the result
        return result


if '__main__' == __name__:
    ListNode1 = ListNode(2)
    ListNode1.next = ListNode(4)
    ListNode1.next.next = ListNode(3)
    ListNode2 = ListNode(5)
    ListNode2.next = ListNode(6)
    ListNode2.next.next = ListNode(4)
    solution = Solution().addTwoNumbers(ListNode1, ListNode2)
    print(solution.val)
    print(solution.next.val)
    print(solution.next.next.val)