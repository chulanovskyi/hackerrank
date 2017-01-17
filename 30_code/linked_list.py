class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 


class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
        if head:
            last_node = head
            while last_node.next:
                last_node = last_node.next
            new_node = Node(data)
            last_node.next = new_node
            return head
        else:
            return Node(data)


if __name__ == '__main__':
	mylist= Solution()
	T=int(input())
	head=None
	for i in range(T):
		data=int(input())
		head=mylist.insert(head,data)
		print(head)
	print(head)
	mylist.display(head);

