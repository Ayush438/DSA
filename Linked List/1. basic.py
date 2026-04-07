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

---------------------------------------------------------
#Find length of Loop

    def lengthOfLoop(self, head):       
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                temp=slow.next
                count=1
                
                while temp!=slow:
                    temp=temp.next
                    count+=1
                return count
        return 0

---------------------------------------------------------
#Odd and even LL
#            The first node is considered odd, and the second node is even, and so on.

def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # store start of even list

        while even and even.next:
            # connect odd nodes
            odd.next = even.next
            odd = odd.next

            # connect even nodes
            even.next = odd.next
            even = even.next

        # attach even list after odd list
        odd.next = even_head

        return head
