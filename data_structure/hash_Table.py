import sys

class HashTable:
    def __init__(self, table_lenght):

        if(table_lenght < 1):
            print("Error: invalid table lenght")
            sys.exit(1)
        else:
            self.__table_lenght = table_lenght
            self.__table = [[] for i in range(self.__table_lenght)]

        

    def __getHash(self, key):
        return key % self.__table_lenght

    def push(self, key):
        self.__table[self.__getHash(key)].append(key)
    

    def show(self):
        for hash_list in self.__table:
            if hash_list:
                for key in hash_list:
                    print('%d ' % key, end=' ')
                print("")

    def find(self, key):
        return ( key in self.__table[self.__getHash(key)])



table = HashTable(9)

table.push(19)
table.push(28)
table.push(20)
table.push(5)
table.push(33)
table.push(15)

table.show()

