'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from typing import Optional, ListNode



class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    if list1 is None:
      return list2
    if list2 is None:
      return list1
    if list1.val < list2.val:
      list1.next = self.mergeTwoLists(list1.next, list2)
      return list1
    else:
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2


if __name__ == '__main__':
  list1 = [1,2,4]
  list2 = [1,3,4]
  print(Solution().mergeTwoLists(list1, list2))