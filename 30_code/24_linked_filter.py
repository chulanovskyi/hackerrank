class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
    def removeDuplicates(self,head):
        filtered = head
        while head.next:
            nxt = head.next
            if nxt.data == head.data:
                after_nxt = nxt.next
                if after_nxt:
                    head.next = after_nxt
                    continue
                else:
                    head.next = None
                    return filtered
            head = nxt
        return filtered


if __name__ == '__main__':
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    head=mylist.removeDuplicates(head)
    mylist.display(head);
