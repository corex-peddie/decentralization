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
                    lst = current_node.get_value()
                    print("Design: {}".format(lst[0]))
                    print("Results: ")
                    print("-"*15)
                    dictionary = lst[-1][-1]
                    for user, num in dictionary.items():
                        print("{user}: {num}".format(user=user, num=num))
                    print("-"*15)
                    print("Date and time added: {}".format(lst[-1][0]))
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
                            lst = current_node.get_value()
                            print("Design: {}".format(lst[0]))
                            print("Results: {}".format(lst[-1][-1]))
                            print("Date and time added: {}".format(lst[-1][0]))

                        current_node = current_node.get_link()
                else:
                    retrieve_collisions += 1
                    return 

    def delete(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        current_ll_value = current_array_value.get_head_node()
        
        if current_ll_value.get_value() == None:
            pass
        elif current_ll_value.get_value()[0] == key:
            self.array[array_index] = BiLinkedList()
        else:
            del_collisions = 1 
            while current_ll_value.get_value()[0] != key:
                new_hash_code = self.hash(key, del_collisions)
                new_array_index = self.compressor(new_hash_code)
                new_array_value = self.array[new_array_index]
                new_ll_value = new_array_valeu.get_head_node()

                if new_ll_value.get_value() == None:
                    pass 
                elif new_ll_value.get_value()[0] == key:
                    self.array[new_array_index] = BiLinkedList()
                    return 
                else:
                    del_collisions += 1
                    return 
        


