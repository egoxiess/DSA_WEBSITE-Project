class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.size += 1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove_at_beginning(self):
        if not self.head:
            return None
        removed = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return removed

    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return removed
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed = self.tail.data
        current.next = None
        self.tail = current
        self.size -= 1
        return removed

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_at_beginning()
        prev = None
        current = self.head
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return None
        prev.next = current.next
        if current == self.tail:
            self.tail = prev
        self.size -= 1
        return current.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.size


if __name__ == "__main__":
    playGame = LinkedList()
    playGame.insert_at_end("play")
    playGame.insert_at_end("pause")
    playGame.insert_at_end("quit")
    playGame.insert_at_end("roll")
    playGame.insert_at_end("duck")
    playGame.insert_at_end("jump")
    playGame.insert_at_end("shoot")
    playGame.insert_at_end("reload")
    playGame.insert_at_end("run")
    playGame.insert_at_beginning("start")

    print(list(playGame))  
    print(playGame.search("call")) 
    print(playGame.remove_at("roll"))
    print(list(playGame))
    print(playGame.remove_at_end())