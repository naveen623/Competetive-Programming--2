"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_element
        else:
            self.head = new_element
        # Your code goes here
        # pass
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp = self.head
        for i in range(1, position):
            if temp.value == None:
                return None
            else:
                temp = temp.next
        return temp.value
        # pass
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if position == 1:
            old = self.head
            new_element.next = old
            self.head = new_element
            return 

        temp = self.head
        for i in range(1, position):
            old = temp.next
            new_element.next = old
            temp.next = new_element
            return
        # pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        if self.head.value == value:
            temp_next = self.head.next
            self.head = temp_next
            return

        temp = self.head
        while temp.next:
            if temp.next.value == value:
                temp_next = temp.next.next
                temp.next = temp_next
                return 
            else:
                temp = temp.next

        # pass
