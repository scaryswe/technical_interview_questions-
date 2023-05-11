#Question

# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.


#Solution with steps

# Define the Node class to represent nodes in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the function to merge two sorted linked lists
def merge_sorted_lists(head1, head2):
    # Base cases: one or both lists are empty
    if not head1:
        return head2
    if not head2:
        return head1
    
    # Recursive case: compare head nodes and merge the remaining nodes
    if head1.data < head2.data:
        head1.next = merge_sorted_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_sorted_lists(head1, head2.next)
        return head2

# Create the first sorted linked list: 1 -> 3 -> 5 -> 7
head_one = Node(1)
head_one.next = Node(3)
head_one.next.next = Node(5)
head_one.next.next.next = Node(7)

# Create the second sorted linked list: 2 -> 4 -> 6 -> 8
head_two = Node(2)
head_two.next = Node(4)
head_two.next.next = Node(6)
head_two.next.next.next = Node(8)

# Merge the two sorted linked lists
merged_head = merge_sorted_lists(head_one, head_two)

# Print the merged linked list
current_node = merged_head
while current_node:
    print(current_node.data, end=' ')
    current_node = current_node.next
