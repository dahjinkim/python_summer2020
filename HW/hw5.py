"""
Class: Python 2020
Homework Assignment 3
Author: Jin Kim
"""

# Initial Node given in the problem
class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)

# help function to translate integer input to node
def NodeFromValue(node, value):
    this_node = node.value
    while this_node != None: # iterate over the entire list
        if this_node.value == value: # if values match
            return this_node
        else:
            this_node = this_node.next # keep iterating


# LinkedList class
class LinkedList():
    def __init__(self, value):
        # takes a number and sets it as the value at the head of the List
        self.value = value
        self.size = 1 # initial length of 1

    def length(self):
        # returns the length of the list
        return print("Length is " + str(self.size))

    def addNode(self, new_value):
        # takes a number and adds it to the end of the list
        # check for correct type
        if type(new_value) != int:
            print("input must be an integer")
        else:
            # create a new node
            new_node = Node(new_value) # make a new node
            # find the end of a list
            # first, create an object for the current node (root)
            this_node = self.value
            # while loop to iterate until end of list (next value = None)
            while this_node.next != None:
                this_node = this_node.next # reset the current node
            # the loop ends when next node is empty
            # time to add the new node
            this_node.next = new_node
            # increase the length
            self.size += 1

    def addNodeAfter(self, new_value, after_node):
        # takes a number and add it after the after_node
        # check for correct type
        if type(new_value) != int:
            print("input must be an integer")
        else:
            # find the afternode from integer input
            afternode = NodeFromValue(node = self, value = after_node)
            # create a new node with value and link
            new_node = Node(_value = new_value, _next = afternode.next)
            # we can insert new node between after_node and its next node
            afternode.next = new_node
            self.size += 1
            print("Added " + str(new_value) + " after " + str(after_node))

    def addNodeBefore(self, new_value, before_node):
        # takes a value and adds it before the before_node
        # check for correct type
        if type(new_value) != int:
            print("input must be an integer")
        else:
            # find the beforenode from integer input
            beforenode = NodeFromValue(node = self, value = before_node)
            # create a new node with value and link
            new_node = Node(_value = new_value, _next = beforenode.value)
            # find a node before the before_node
            # set current node
            this_node = self.value
            # if you want to insert before the first node
            if this_node == beforenode:
                new_node.next = this_node # make the connection
                self.value = new_node # reset the root node
            else:
                while this_node.next != beforenode:
                    this_node = this_node.next
                    # we can insert new node between this_node and before_node
                this_node.next = new_node
            self.size += 1
            print("Added " + str(new_value) + " before " + str(before_node))

    def removeNode(self, node_to_remove):
        # find the node_to_remove
        # transform integer into node
        that_node = NodeFromValue(node = self, value = node_to_remove)
        this_node = self.value
        # if you want to remove the first node
        if this_node == that_node:
            self.value = this_node.next # reset the root to the next node
        else:
            # iterate until we find the previous node of the node to remove
            while this_node.next != that_node:
                this_node = this_node.next
            # make a link that skips that_node
            this_node.next = that_node.next
        self.size -= 1
        print("Removed " + str(that_node.value))


    def removeNodeByValue(self, value):
        # takes a value and removes all nodes with that value
        this_node = self.value
        while this_node.next != None: # iterate over the whole list
            if this_node.value == value: # if value matches
                self.removeNode(this_node.value)
            this_node = this_node.next


    def reverse(self):
        # reverses the order of the linked list
        previous_node = None # start with an empty node
        this_node = self.value # get root node
        while this_node != None: # iterate over the whole list
            next_node = this_node.next # save the next node
            this_node.next = previous_node # switch place
            previous_node = this_node # switch place
            this_node = next_node # move on to the next node
        self.value = previous_node # reset the root
        print("Reversed")

    def __str__(self):
        # displays the list in some reasonable way
        lists = ""
        this_node = self.value
        while this_node != None:
            lists += str(this_node.value) + " "
            this_node = this_node.next
        return lists

# All of these functions iterate over the list until they find some match
# and execute some move. This is essentially iterating n-1 times and make 1 move,
# which is complexity O(n). I think it is the best possible complexity class.

##### Tests
first_node = Node(5)
my_list = LinkedList(first_node)
my_list.addNode(25)
my_list.addNode(5)
my_list.addNode(5)
print(my_list) # should print 5 25 5 5
my_list.length() # should be 4
my_list.addNode("Mon") # should throw error message
my_list.addNodeBefore(9, 5)
my_list.addNodeAfter(2, 5)
my_list.reverse()
print(my_list) # should print 5 5 25 2 5 9
my_list.removeNode(5) # removes the first instance of 5
my_list.removeNodeByValue(5) # removes all five
print(my_list) # should print 25 2 9
my_list.length() # should be 3
