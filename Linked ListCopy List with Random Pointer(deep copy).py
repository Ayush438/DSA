#https://leetcode.com/problems/copy-list-with-random-pointer/description/


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        temp=head
        new_node={}

        while temp:      
            new_node[temp]=Node(temp.val)
            temp=temp.next

        temp=head

        while temp:
            new_node[temp].next=new_node.get(temp.next)
            new_node[temp].random=new_node.get(temp.random)
            temp=temp.next

        return new_node[head]
