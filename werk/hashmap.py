#design hashMao

class LinkedNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [None for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        pos = key % 1000
        
        if self.array[pos] == None:
            self.array[pos] = LinkedNode(key,value)
        else:
            cur = self.array[pos]
            
            if cur.key == key:
                cur.val = value
            else:    
                while cur.next:
                    if cur.next.key == key:
                        cur.next.val = value
                        return
                    cur = cur.next
                
                cur.next = LinkedNode(key,value) 
            

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        pos = key % 1000
        
        if self.array[pos] == None:
            return -1
        else:
            cur = self.array[pos]
            while cur:
                if cur.key == key:
                    return cur.val
                cur = cur.next
            
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        pos = key % 1000
        
        if self.array[pos] != None:
            cur = self.array[pos]
            if cur.key == key:
                self.array[pos] = cur.next
            else:
                while cur.next:
                    if cur.next.key == key:
                        cur.next = cur.next.next
                        return
                    cur = cur.next
