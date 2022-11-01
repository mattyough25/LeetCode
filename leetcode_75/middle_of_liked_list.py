'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
	slow = head #this will go forward 1 at a time
	fast = head #move forward 2 at a time
	while fast and fast.next: #while our fast node exists and isn't the last node
		slow = slow.next #slow pointer moves forward just 1 spot
		fast = fast.next.next #fast pointer moves forward by two
	return slow #slow should be in the middle!