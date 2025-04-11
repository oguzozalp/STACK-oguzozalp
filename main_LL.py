# main_LL.py

from ds import Stack, LinkedListNode

def main_LL():
    stack = Stack()

    print("Pushing 10, 20, 30 onto the stack...")
    stack.push(LinkedListNode(10))
    stack.push(LinkedListNode(20))
    stack.push(LinkedListNode(30))

    print("Top of stack (peek):", stack.peek().data)

    print("Popping top of stack...")
    popped_node = stack.pop()
    print("Popped:", popped_node.data)

    print("Top of stack now:", stack.peek().data)

if __name__ == "__main__":
    main_LL()
