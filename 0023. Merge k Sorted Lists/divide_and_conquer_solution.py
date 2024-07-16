# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case for empty list, simply return None
        if not len(lists):
            return None
        # base case for merging one list, simply return the list as it is already sorted
        elif len(lists) == 1:
            return lists[0]
        # base case for merging two lists, compare the beginning of the lists to see which is less, then add it to a result list until we exhaust all options for both lists
        elif len(lists) == 2:
            list1 = lists[0]
            list2 = lists[1]

            result = ListNode(-1)
            iterNode = result
            while list1 and list2:
                if list1.val < list2.val:
                    iterNode.next = list1
                    list1 = list1.next
                else:
                    iterNode.next = list2
                    list2 = list2.next
                iterNode = iterNode.next
            if list1:
                iterNode.next = list1
            if list2:
                iterNode.next = list2
            return result.next
        # split up the list of lists into two equal parts to perform divide and conquer. then merge the two resulting lists
        else:
            result1 = self.mergeKLists(lists[:len(lists)//2])
            result2 = self.mergeKLists(lists[len(lists)//2:])
            return self.mergeKLists([result1, result2])