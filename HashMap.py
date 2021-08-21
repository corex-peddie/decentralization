from BiLinkedList import BiLinkedList

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size 
        self.array = [BiLinkedList() for i in range(self.array_size)]
    
    def hash(self, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size 

    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_value = current_array_value.get_head_node()

        if current_ll_value.get_value() == None:
            self.array[array_index] = BiLinkedList([key, value])
            return 
        elif current_ll_value.get_value()[0] == key:
            self.array[array_index].add_to_head([key, value])
            return 
        else:
            number_collisions = 1 
            while current_ll_value.get_value()[0] != key:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]
                new_ll_value =  new_array_value.get_head_node()

                if new_ll_value.get_value() == None:
                    self.array[new_array_index] = BiLinkedList([key, value])
                    return 
                elif new_ll_value.get_value()[0] == key:
                    self.array[new_array_index].add_to_head([key, value])
                    return 
                else:
                    number_collisions += 1
                    return 
    
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_value = current_array_value.get_head_node()

        if current_ll_value.get_value() == None:
            return None 
        elif current_ll_value.get_value()[0] == key:
            current_node = current_ll_value 
            while current_node:
                if current_node.get_value() != None:
                    print(current_node.get_value())
                current_node = current_node.get_link()
        else:
            retrieve_collisions = 1
            while current_ll_value.get_value()[0] != key:
                new_hash_code = self.hash(key, retrieve_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]
                new_ll_value = new_array_value.get_head_node()

                if new_ll_value.get_value() == None:
                    return None 
                elif new_ll_value.get_value()[0] == key:
                    current_node = new_ll_value 
                    while current_node:
                        if current_node.get_value() != None:
                            print(current_node.get_value())
                        current_node = current_node.get_link()
                else:
                    retrieve_collisions += 1
                    return 


hashmap = HashMap(5)


# Logo 1
hashmap.setter('a', 'b')
hashmap.setter('a', 'c')

# Logo 2
hashmap.setter('b', 'c')


hashmap.retrieve('a')
hashmap.retrieve('b')