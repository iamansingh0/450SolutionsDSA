# code
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None


def reverseLL(head):
    """function to reverse the linked list"""
    # taking some pointers
    curr = head
    prev = None
    # looping until the list becomes empty
    while curr:
        nextNode = curr.next
        # direction of link is changed
        curr.next = prev
        # pointers are updated for next iteration
        prev = curr
        curr = nextNode
    # returning the prev which is the new head
    return prev


def isPalindrome(head):
    # if the head is empty or has only one node,
    # it is already a palindrome
    if head is None or head.next is None:
        return True
    # taking some pointers
    mid = tail = head
    # mid node is found out using slow and fast pointers
    while tail and tail.next:
        mid = mid.next
        tail = tail.next.next
    # list is reversed after mid node
    revCurr = reverseLL(mid)
    # looping until the newHead becomes empty
    while revCurr:
        # checking if the data does not match between the two
        # and if it isn't returning False
        if revCurr.data != head.data:
            return False
        # updating the pointers for next iteration
        head = head.next
        revCurr = revCurr.next
    # else all the data are matched, so returning True
    return True

# question link
# https://www.codingninjas.com/studio/problems/palindrom-linked-list_799352