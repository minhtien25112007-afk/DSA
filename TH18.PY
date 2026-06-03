class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def bubble_sort_linked_list(head):
    if head is None:
        return head

    swapped = True

    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = \
                current.next.data, current.data

                swapped = True

            current = current.next

    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


# 1 -> 3 -> 2
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)

head = bubble_sort_linked_list(head)
print_list(head)