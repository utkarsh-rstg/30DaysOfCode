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
    #Complete this method
        n1= Node(data)
        if head==None:
            head=n1
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next=n1
        n1.next=None
        return head
    
mylist= Solution()