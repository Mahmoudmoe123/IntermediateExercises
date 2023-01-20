def adddictstogether(firstdict, seconddict):
    addeddict = {}

    for x in firstdict:
        if x in seconddict:
            addeddict[x] = firstdict[x]+seconddict[x]

    return addeddict


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = adddictstogether(my_dict_1, my_dict_2)
print(combined_dict)


