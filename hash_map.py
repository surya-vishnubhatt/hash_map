from unordered_list import UnorderedList

class HashMap:
    def __init__(self, table_size=11, can_rehash=False):
        # TODO: Implement. Add any member variables that
        # you feel are necessary.
        self.can_rehash = can_rehash
        self.table_size = table_size
        self.table = [UnorderedList() for i in range (self.table_size)] #makes a table of unordered lists
        self.counter = 0
    def get_table_size(self):
        # TODO: Implement.
        return self.table_size

    def get_num_keys(self):
        #MUST TAKE CONSTANT TIME! FIND THE NUMBER OF KEYS!
        return self.counter

    def get_load_factor(self):
        # TODO: Implement.
        return (self.get_num_keys())/(self.table_size)

    def hash_function(self,key):
        return key % self.table_size

    def isPrime(self,double_val): #I referenced the following source to create this function: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
        for i in range(2,int(double_val**0.5)+1):
            if double_val%i==0:
                return False
        return True

    def insert(self, key, value): #WE MODIFY FOR REHASHING
        index = self.hash_function(key)
        double_val = 2*self.table_size
        while self.isPrime(double_val) != True:
            double_val += 1
        if key in self.table[index].keylist:
            raise ValueError("Key already mapped")
        else:
            self.table[index].add(key, value) #key and value when adding to index? need modify
            self.counter += 1
            if self.get_load_factor() >= 0.5 and self.can_rehash == True:
                self.table_size = double_val #set to the next big prime number that is 2 times double val
                keyvalues_1 = []
                val_values = []
                for i in range(len(self.table)):
                    if self.table[i].isEmpty() != True:
                        size_val = self.table[i].size()
                        current = self.table[i].head
                        for j in range(size_val):
                            keyvalues_1.append(current.key) #get all of the keys
                            val_values.append(current.value) #get all the values
                            current = current.getNext()
                self.table = [UnorderedList() for i in range (self.table_size)] #update the table for the new size
                incrementer = 0
                for key in keyvalues_1:
                    index = self.hash_function(key)
                    self.table[index].add(key, val_values[incrementer])
                    incrementer += 1

    def find(self, key):
        index = self.hash_function(key)
        return self.table[index].find(key)

    def update(self, key, value): #update the value at the given key
        index = self.hash_function(key)
        if key not in self.table[index].keylist:
            raise ValueError("Key not mapped")
        else:
            current = self.table[index].head #need to overwrite the current value
            while current.key != key:
                current = current.getNext()
            if current.key == key:
                current.setValue(value)

    def delete(self, key):
        # TODO: Implement. IF KEY NOT MAPPED DELETE DOES NOTHING
        index = self.hash_function(key)
        if key not in self.table[index].keylist:
            return
        else:
            self.counter -= 1
            self.table[index].remove(key)
            self.table[index].keylist.remove(key)


    def print_keys(self):
        end = False
        for i in range(len(self.table)):
            newlist = []
            if self.table[i].isEmpty() == True:
                print(str(i) + ":" + " " + str(None))
            else:
                size_val = self.table[i].size()
                current = self.table[i].head
                for j in range(size_val):
                    newlist.append(str(current.key))
                    current = current.getNext()
                print(str(i) + ":" + " " + (" ").join(newlist))


    def __contains__(self, key): #The IN operator
        # TODO: Implement.
        keyvalues = []
        for i in range(len(self.table)):
            if self.table[i].isEmpty() != True:
                size_val = self.table[i].size()
                current = self.table[i].head
                for j in range(size_val):
                    keyvalues.append(current.key)
                    current = current.getNext()
        if key in keyvalues:
            return True
        else:
            return False


if __name__ == "__main__":
    h = HashMap()
    h.insert(3, 8)
    h.insert(14, 15)
    h.insert(50, 20)
    h.insert(27, -5)
    h.insert(36, 40)
    print("=== Printing keys ===")
    h.print_keys()
    print("=== Done printing keys ===")
    print("h.get_num_keys():", h.get_num_keys())
    print("h.find(3):", h.find(3))
    print("h.find(36):", h.find(36))
    print("h.find(20):", h.find(20))
    print("3 in h:", 3 in h)
    print("36 in h:", 36 in h)
    print("40 in h:", 40 in h)  # value doesn't work
    h.delete(3)
    h.delete(36)
    h.delete(80)  # unsuccessful
    print("=== Performed three deletions (two successful) ===")
    h.print_keys()
    print("=== By default, rehashing is disabled ===")
    h.insert(11, 1)
    h.insert(22, 1)
    h.insert(33, 1)
    h.print_keys()
    print("h.get_num_keys():", h.get_num_keys())
    print("Load factor (rounded):", round(h.get_load_factor(),2))
    print("\n=== Let's try a hash table that supports rehashing ===")
    h = HashMap(5, True)
    h.insert(15, "values can be any type, by the way")
    h.insert(20, "but the keys have to be integers")
    print("===== Before insertion that causes rehash =====")
    h.print_keys()
    h.insert(26, 48)  # triggers rehashing, AFTER being inserted
    print("===== After rehashing =====")
    h.print_keys()
    print("h.get_num_keys():", h.get_num_keys())
    print("Load factor (rounded):", round(h.get_load_factor(),2))