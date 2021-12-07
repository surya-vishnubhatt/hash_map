# Initial version from section 4.21 of "Problem Solving with Algorithms and Data
# Structures using Python" by Brad Miller and David Ranum.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def setKey(self, key):
        self.key = key
    def setValue(self, value):
        self.value = value

class UnorderedList:
    def __init__(self):
        self.head = None
        self.keylist = []
    def isEmpty(self):
        return self.head == None
    def add(self,key, value):
        self.keylist.append(key)
        temp = Node(key)
        temp.setNext(self.head)
        self.head = temp
        self.head.setValue(value)
        self.head.setKey(key)
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count
    def find(self,key):
        current = self.head
        found = False
        while current != None and not found:
            if current.key == key:
                found = True
            else:
                current = current.getNext()
        if found == True:
            return current.value
        else:
            return None
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    # Added by me, from slide 42 of the linear data structures slide deck.
    # Prints the values in this unordered list in the order in which
    # they appear, starting from the front.
    def printAll(self):
        current = self.head
        while current != None:
            print(current.getData(), end=' ')
            current = current.getNext()
        print()

if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    mylist.printAll()
    print(mylist.size())
    mylist.add(100)
    mylist.printAll()
    print(mylist.size())
    mylist.remove(54)
    mylist.printAll()
    print(mylist.size())
    mylist.remove(93)
    mylist.printAll()
    print(mylist.size())
    mylist.remove(31)
    mylist.printAll()
    print(mylist.size())