"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
- Advantages over SLL - IT can be traversed in both forward and backward direction.
    Delete operation is more efficient.
"""


class Link:
    next = None  # This points to the link in front of the new link
    previous = None  # This points to the link behind the new link

    def __init__(self, x):
        self.value = x

    def displayLink(self):
        print(self.value, end=" ")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, x):
        new_link = Link(x)  # Create a new link with a value attached to it
        if self.is_empty():  # Set the first element added to be the tail
            self.tail = new_link
        else:
            self.head.previous = new_link  # new_link <-- currenthead(head)
        new_link.next = self.head  # new_link <--> currenthead(head)
        self.head = new_link  # new_link(head) <--> oldhead
        self.size += 1

    def delete_head(self):
        temp = self.head
        self.head = self.head.next  # oldHead <--> 2ndElement(head)
        self.head.previous = None  # oldHead --> 2ndElement(head) nothing pointing at it so the old head will be removed
        if not self.head:
            self.tail = None  # if empty linked list
        self.size -= 1
        return temp

    def insert_tail(self, x):
        newLink = Link(x)
        newLink.next = None  # currentTail(tail)    newLink -->
        self.tail.next = newLink  # currentTail(tail) --> newLink -->
        newLink.previous = self.tail  # currentTail(tail) <--> newLink -->
        self.tail = newLink  # oldTail <--> newLink(tail) -->
        self.size += 1

    def delete_tail(self):
        temp = self.tail
        self.tail = self.tail.previous  # 2ndLast(tail) <--> oldTail --> None
        self.tail.next = None  # 2ndlast(tail) --> None
        self.size -= 1
        return temp

    def delete(self, x):
        current = self.head

        while current.value != x:  # Find the position to delete
            current = current.next

        if current == self.head:
            self.deleteHead()
        elif current == self.tail:
            self.deleteTail()
        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        self.size -= 1

    def is_empty(self):  # Will return True if the list is empty
        return self.head is None

    def display(self):  # Prints contents of the list
        current = self.head
        while current:
            current.displayLink()
            current = current.next
        print()

    def __len__(self):
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_head("a")
        >>> len(linked_list)
        1
        >>> linked_list.insert_tail("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        return self.size
