    
class Node:
    prev = None
    def __init__(self, value):
        self.data = value

class Stack:
    top = None

    def push(self, value):
        new = Node(value)
        if top:
            new.prev = top

        top = new
        return None

    def pop(self):
        if top:
            ret = top
            top = top.prev
            return ret.data

        return None

    def peek(self):
        if top:
            return top.data
        return None


class Queue:
    first = None
    last = None

    def enqueue(self, value):
        new = Node(value)
        if last:
            last.prev = new
        else:
            first = new
        last = new 

    def dequeue(self):
        if first:
            ret = first.data
            first = first.prev
            return ret
        return None






