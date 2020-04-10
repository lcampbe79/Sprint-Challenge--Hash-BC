#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(length):

        #retrieve takes the hash table and key for every index, finds weight_list_key corresponding to key
        #limit - weight[i] = another weight[i] or a key! 
        #weight_list_key will return none if key is not found, otherwise retrieves the weight_list_key stored with the key 
        weight_list_key = hash_table_retrieve(ht, (limit - weights[i]))
        #populate the hash table, storing the weight_list_key w/ the given key 
        hash_table_insert(ht, weights[i], i)

        #i and weight_list_key are indices of two weights that equal the limit
        if weight_list_key is not None:
            # The higher value index (weight_list_key) should be placed in the zeroth index and the smaller index should be placed in the first index. 
            if i > weight_list_key:
                return [i, weight_list_key]
            else:
                return [weight_list_key, i]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
