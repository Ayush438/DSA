# Middle of LL

def find_middle(head):
    slow = head   
    fast = head   
    while fast and fast.next and slow:
        fast = fast.next.next 
        slow = slow.next       

    return slow  
------------------------------------------------------
#Reverse LL
    def reverseList(self, head):
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev
---------------------------------------------------------
#starting-point-of-loop-in-a-linked-list
def detectCycle(self, head):
        slow = head                                    
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
#When they meet first, the fast pointer has travelled extra distance equal to full loop cycles.
#Because of this, the distance from head to loop start becomes equal to the distance from meeting point to loop start.
#So if one pointer starts from head and the other from the meeting point, and both move one step at a time,
#They will meet exactly at the starting node of the loop.
