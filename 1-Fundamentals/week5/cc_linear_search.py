def linear_search_dictionary(my_dictionary, target):
    for x in range(len(my_dictionary.values())):
        if (list(my_dictionary.values()))[x] == target:
            print("Found at key:", (list(my_dictionary.keys()))[x])
            return x
    print("Target is not in the dictionary")
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
