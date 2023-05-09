# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node and a current node to use for merging
        cur = dummy = ListNode()
        # Loop through both linked lists as long as neither one is empty
        while list1 and list2:
            # If the value of the current node in list1 is smaller, add it to the merged list
            if list1.val < list2.val:
                cur.next = list1
                # Move to the next node in list1
                list1, cur = list1.next, list1
            # If the value of the current node in list2 is smaller, add it to the merged list
            else:
                cur.next = list2
                # Move to the next node in list2
                list2, cur = list2.next, list2
        # Once we've reached the end of one of the lists, add the remaining nodes from the other list to the merged list
        if list1 or list2:
            cur.next = list1 if list1 else list2
        # Return the head of the merged list
        return dummy.next
