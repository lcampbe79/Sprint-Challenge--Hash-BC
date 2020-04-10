#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for t in tickets:
        #inserts each ticket into the hash table based on key
        hash_table_insert(hashtable, t.source, t.destination)

    starting_point = "NONE"
    #loops through every item in hash table
    for i in range(length):
        #route is set equal to hash_table_retrieve
        route[i] = hash_table_retrieve(hashtable, starting_point)
        #Starting point is equal to the route[0] route[1]
        starting_point = route[i]
    #Gets rid of None
    return route[:len(route)-1] 
