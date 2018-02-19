__author__ = 'David'

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
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current=self.head
        current_pos=1
        while current:
            if current_pos==position:
                return current
            current = current.next
            current_pos+=1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current=self.head
        current_pos=1
        while current:
            if current_pos+1==position:
                new_element.next=current.next
                current.next=new_element
                break
            else:
                current_pos+=1
                current=current.next



    def delete(self, value):
        """Delete the first node with a given value."""
        current=self.head
        if current.value==value:
            self.head=current.next
            return
        while current.next:
            if current.next.value==value:
                current.next=current.next.next
                break

