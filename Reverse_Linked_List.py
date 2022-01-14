class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        currentNode = head
        prev = None
        nextNode = None
        
        while currentNode != None:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        head = prev
        return head