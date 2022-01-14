class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    def append(self, new_data):
 
        new_node = Node(new_data)
 
        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while (last.next):
            last = last.next
 
        last.next =  new_node

    def hasCycle(self, head):
    
        
        node_seen = set()
        
        curr = head
        
        while curr != None:
            if curr in node_seen:
                return True  
            node_seen.add(curr)
            curr = curr.next
            
        return False


        ####### Efficinet Algo using Floyed Cycle detecting algo in O(1) space complexity ####

        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

