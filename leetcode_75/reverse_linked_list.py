'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
######################################################################################
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
 ################################################################################           
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr= head
        prev= None
        while curr!= None:
            next= curr.next
            curr.next= prev
            prev= curr
            curr= next
        return prev

# Test Cases
s = Solution()
head = ListNode([1,2,3,4,5])
out = s.reverseList(ListNode([1,2,3,4,5]))
print(out.val)

'''
s = Solution()
head = ListNode(1,2)
out = s.reverseList(head)
print(out)

s = Solution()
head = ListNode()
out = s.reverseList(head)
print(out)
'''