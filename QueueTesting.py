__author__ = 'David'

from Collections import Queue,Element

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)

q = Queue(e1)
q.enqueue(e2)
q.enqueue(e3)

# Test peek
# Should be 1
print (q.peek().value)

# Test dequeue
# Should be 1
print (q.dequeue().value)

# Test enqueue
q.enqueue(e4)
# Should be 2
print (q.dequeue().value)
# Should be 3
print (q.dequeue().value)
# Should be 4
print (q.dequeue().value)
q.enqueue(e5)
# Should be 5
print (q.peek().value)