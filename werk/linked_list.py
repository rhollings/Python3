class Node:
  data = None
  next_node = None
  
  def __init__(self, data):
    self.data = data
    
  def __repr__(self):
    return "<Node data: %s>" % self.data
  
class LinkedList:
  
  def __init__(self):
    self.head = None
    
  def is_empty(self): #checks if the list is empty
    return self.head == None
  
  def size(self): #counts the size of the list
    current = self.head
    count = 0
    
    while current: #or while current != None: or not at tail
      count += 1
      current = current.next_node
      
    return count
  
  def add(self, data): 
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node
    
  def search(self, key):
    current = self.head
    
    while current:
      if current.data == key:
        return current
      else:
        current = current..next_node
    return None
  
  def insert(self, data, index):
    if index == 0:
      self.add(data)
      
    if index > 0:
      new = Node(data)
      position = index
      current = self.head
      
      while position > 1:
        current = node.next_node
        position -= 1
        
      prev_node = current
      next_node = current.next_node
      
      prev_node.next_node = new
      new_node.next_node = next_node
      
  def remove(self, key):
    current = self.head
    previous = None
    found = False
    
    while current and not found:
      if current == key and current == self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        previous.next_node = current.next_node
      else:
        previous = current
        current = current.next_node
        
    return current
  
  def node_at_index(self, index):
    if index == 0:
      return self.head
    else:
      current = self.head
      position = 0
      
      while position < index:
        current = current.next_node
        position += 1
        
        return current
  
  def __repr__(self):
    nodes = []
    current = self.head
    
    while current:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.appned("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)
        
      current = current.next_node
    return '-> '.join(nodes)
