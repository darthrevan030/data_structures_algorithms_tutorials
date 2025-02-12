class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node data: %s>" % self.data

class Linked_List:
# Singly linked list
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def llSize(self):
        current = self.head
        size = 0

        while current:
            size += 1
            current = current.next
        return size

    def addNodeToStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def findNodeData(self, key): #searches for node based on data contained in the Node
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next
        
        return None

    def insertNewNode(self, data, index):
        if index == 0:
            self.addNodeToStart(data)
            return

        if index > 0:
            newNode = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next
                position -= 1

            prevNode = current
            nextNode = current.next

            prevNode.next = newNode
            newNode.next = nextNode

    def removeNodeByKey(self, key):
        current = self.head
        prev = None
        found = False

        while current and not found:
            # base case - node is the head node
            if current.data == key and current is self.head:
                found = True
                self.head = current.next # reassign head to the next node
                #del current #delete current
                break
            # reassign pointer from the previous node to the next node - essentially skips the node we want to remove
            elif current.data == key:
                found = True
                prev.next = current.next
            # if the current node is not the node we are looking for, keep traversing the ll until node is found
            else: 
                prev = current
                current = current.next
                
        return current
    
    def removeNodeByIndex(self, index):
        return



    def __repr__(self): # aka print list
        nodes =[]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else: 
                nodes.append("[%s]" % current.data)
            current = current.next
        
        return "->".join(nodes)

##################################################################################################################

# instantiate linked list
ll = Linked_List()

# add nodes to linked list
ll.addNodeToStart(1)
ll.addNodeToStart(2)
ll.addNodeToStart(3)
ll.addNodeToStart(55)
ll.addNodeToStart(7)

ll.insertNewNode(6665, 0)
ll.insertNewNode(74747474, 5)
ll.insertNewNode(45, 6)


print(ll.llSize())
print(ll)
print(ll.findNodeData(55))
print(ll.findNodeData(45))

ll.removeNodeByKey(55)
print(ll)
