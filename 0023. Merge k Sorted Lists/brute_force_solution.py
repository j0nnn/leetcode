# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(-1)
        iterNode = result
        # while there are still elements in the lists continue iterating
        while lists:
            minimum = None
            # find minimum of all the beginninig of the lists
            for i, l in enumerate(lists):
                if l == None: continue
                if minimum == None:
                    minimum = i
                elif lists[minimum].val > l.val:
                    minimum = i
            # base case if no minimum was found (everything is empty)
            if minimum == None: break
            # add the minimum list to the result linked list and move the pointer of the result list and added list
            iterNode.next = lists[minimum]
            iterNode = iterNode.next
            # pop list from lists if it is empty
            if lists[minimum].next != None:
                lists[minimum] = lists[minimum].next
            else:
                lists.pop(minimum)
        return result.next
