from typing import Optional


class Node:
    def __init__(self, data: Optional[int] = None) -> None:
        """Initialize a node with data.

        :param data: The value of the node.
        """
        self.data: Optional[int] = data
        self.next: Optional["Node"] = None  # Pointer to the next node


class LinkedList:
    def __init__(self) -> None:
        """Initialize an empty linked list."""

        self.head: Optional[Node] = None

    def insert_at_beginning(self, data: int) -> None:
        """Insert a new node at the beginning of the list.

        :param data: The value to insert.
        """
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point new node's next to current head
        self.head = new_node  # Make new node the new head

    def insert_at_end(self, data: int) -> None:
        """Insert a new node at the end of the list.

        :param data: The value to insert.
        """
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, new node becomes head
        else:
            cur = self.head
            # Traverse to the last node
            while cur.next:
                cur = cur.next
            cur.next = new_node  # Add new node at the end

    def insert_after(self, prev_node: Node, data: int) -> None:
        """Insert a new node after a given node.

        :param prev_node: The node after which new node is inserted.
        :param data: The value to insert.
        """
        if prev_node is None:
            print("The given previous node does not exist.")
            return
        new_node = Node(data)  # Create a new node
        new_node.next = prev_node.next  # Point new node's next to previous node's next
        prev_node.next = new_node  # Link previous node to the new node

    def delete_node(self, key: int) -> None:
        """Delete the first node that has the given value.

        :param key: The value to be deleted.
        """
        cur = self.head

        # If head node holds the key to be deleted
        if cur and cur.data == key:
            self.head = cur.next  # Change head to next node
            cur = None  # Free old head
            return

        prev: Optional[Node] = None
        # Search for the node with the key value
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        # If the key was not found, do nothing
        if cur is None:
            return

        # Unlink the node from the linked list
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Optional[Node]:
        """Search for a node with the given value.

        :param data: The value to search for.
        :return: The node if found, otherwise None.
        """
        cur = self.head
        while cur:
            if cur.data == data:
                return cur  # Node found
            cur = cur.next
        return None  # Not found

    def print_list(self) -> None:
        """Print the linked list"""

        current = self.head
        # Traverse the list and print each node's data
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

    def reverse(self) -> None:
        """Reverse the linked list."""
        prev: Optional[Node] = None
        current = self.head
        # Change next of each node to previous node
        while current:
            next_node = current.next  # Save next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current node
            current = next_node  # Move to next node
        self.head = prev  # Update head to the new first node

    def sorted_insert(self, new_node: Node) -> None:
        """Insert a node into the sorted linked list.

        :param new_node: The node to insert.
        """
        # If the list is empty or new node should be first
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            # Find the node after which new_node should be inserted
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self) -> None:
        """
        Sort the linked list using insertion sort.
        """
        sorted_list = LinkedList()  # Create a new empty sorted list
        current = self.head
        # Traverse the original list and insert nodes in sorted order
        while current:
            next_node = current.next  # Save next node
            current.next = None  # Disconnect the node from the list
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head  # Update head to the sorted list's head


def merge_sorted_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    """Merge two sorted linked lists into one sorted list.

    :param list1: The head node of the first sorted list.
    :param list2: The head node of the second sorted list.
    :return: The head node of the merged sorted list.
    """
    dummy = Node()  # Create a dummy node to start the merged list
    tail = dummy  # Tail will point to the last node in the merged list

    # Compare nodes from both lists and attach the smaller node
    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Attach the remaining nodes, if any
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next  # Return the merged list, skipping dummy node


if __name__ == "__main__":

    # Create first sorted linked list: 1 -> 3 -> 5
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    # Create second sorted linked list: 2 -> 4 -> 6
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    # Merge two sorted lists
    merged_list_head = merge_sorted_lists(llist1.head, llist2.head)
    merged_list = LinkedList()
    merged_list.head = merged_list_head

    print("Merged sorted list:")
    merged_list.print_list()

    # Create linked list: 5 -> 10 -> 15 -> 20 -> 25
    llist = LinkedList()
    for i in [5, 10, 15, 20, 25]:
        llist.insert_at_end(i)

    print(f"Linked list:")
    llist.print_list()
    # Reverse linked list
    llist.reverse()
    print("Linked list after reversing:")
    llist.print_list()

    # New unsorted linked list
    llist = LinkedList()
    for i in [25, 5, 20, 10, 15]:
        llist.insert_at_end(i)

    print(f"Linked list before insertion sort:")
    llist.print_list()
    # Sort linked list using insertion sort
    llist.insertion_sort()
    print(f"Linked list after insertion sort:")
    llist.print_list()
