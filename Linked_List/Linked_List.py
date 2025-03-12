class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
             self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        pass

    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
             self.tail.next = new_node
        else:  
            self.head = new_node
        self.tail = new_node
        pass

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.prev = None
        else:
            self.head = None
        return removed_value
    
# Criando uma instância da lista 
dll = DoublyLinkedList()

# Adicionando elementos na frente
dll.add_to_front(10)
dll.add_to_front(20)
dll.add_to_front(30)

print("Após adicionar ao início:", dll.head.value, dll.tail.value)  

# Adicionando elementos ao final
dll.add_to_end(40)
dll.add_to_end(50)

print("Após adicionar ao final:", dll.head.value, dll.tail.value)  

# Removendo do início
removed_front = dll.remove_from_front()
print("Removido do início:", removed_front)  #

print("Novo início:", dll.head.value)  

# Removendo do final
removed_end = dll.remove_from_end()
print("Removido do final:", removed_end)  

print("Novo final:", dll.tail.value)  

# Removendo todos os elementos
dll.remove_from_front()
dll.remove_from_front()
dll.remove_from_front()

print("Lista vazia?", dll.head is None, dll.tail is None)


         