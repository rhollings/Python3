# Merge 2 sorted linked lists

def __init__(self, val=0, next=None):
  self.val = val
  self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
  dummy = ListNode()
  tail = dummy
  
  while l1 and l2:
    if l1.val < l2.val:
      tail.next = l1
      l1 = l1.next
    else:
      tail.next = l2
      l2 = l2.next
      
    tail = tail.next
    
    if l1:
      tail.next = l1
    elif l2:
      tail.next = l2
      
    return dummy

  
  def mergeLists(head1, head2):
    if head1==None and head2==None:
        return head1
    if head1==None:
        return head2
    if head2==None:
        return head1
    
    res=SinglyLinkedListNode(None)
    c=res
    c1=head1
    c2=head2
    while c1!=None and c2!=None:
        if c1.data<=c2.data:
            c.next=c1
            c1=c1.next
        else:
            c.next=c2
            c2=c2.next
        c=c.next
    
    if c1!=None:
        c.next=c1
    if c2!=None:
        c.next=c2
    return res.next
