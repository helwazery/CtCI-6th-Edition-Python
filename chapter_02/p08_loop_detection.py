#Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
#beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
#as to make a loop in the linked list.
#EXAMPLE
#Input: A -) B -) C -) 0 -) E - ) C[thesameCasearlierl
#Output: C
#----------------------------------------------------------------------------------------------------------------------
from chapter_02.linked_list import LinkedList


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected
