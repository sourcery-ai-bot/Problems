class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next_node(self, node):
        self.next_node = node


class LinkedList:
    def __init__(self, *args):

        self.last_node_touched = None
        for value in reversed([*args]):
            new_node = Node(value)
            new_node.set_next_node(self.last_node_touched)
            self.last_node_touched = new_node

    def prepend(self, x):
        new_node = Node(x)
        new_node.set_next_node(self.last_node_touched)
        self.last_node_touched = new_node

    def __str__(self):
        visited_node = self.last_node_touched
        output_string = str(visited_node.value)
        while visited_node.next_node is not None:
            visited_node = visited_node.next_node
            output_string += str(visited_node.value)
        return output_string

    def go_to_next_node(self):
        self.last_node_touched = self.last_node_touched.next_node

    def reverse(self):
        previous_node = None
        while self.last_node_touched.next_node is not None:
            next_node = self.last_node_touched.next_node
            self.last_node_touched.next_node = previous_node
            previous_node = self.last_node_touched
            self.last_node_touched = next_node

        self.last_node_touched.next_node = previous_node

    def rotate(self, k):
        first_node = self.last_node_touched
        current_node = self.last_node_touched
        count = 0
        while current_node.next_node:
            current_node = current_node.next_node
            count += 1
        current_node.set_next_node(first_node)
        count -= k
        while count >= 0:
            current_node = current_node.next_node
            count -= 1
        next_node = current_node.next_node
        current_node.next_node = None
        self.last_node_touched = next_node



def reverse(linked_list):
    new_list = LinkedList(linked_list.last_node_touched.value)
    head = linked_list.last_node_touched
    while head.next_node is not None:
        new_list.prepend(head.next_node.value)
        head = head.next_node
    return new_list


ell_ell = LinkedList(2,3,4,5,6)
ell_ell.prepend(1)

print(ell_ell)

ell_ell.reverse()
print(ell_ell)

function_reversed_list = reverse(ell_ell)
print(function_reversed_list)


"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

"""
emm_emm = LinkedList(1,2,3,4,5,6)
emm_emm.rotate(3)

print(emm_emm)
emm_emm.rotate(2)
print(emm_emm)
