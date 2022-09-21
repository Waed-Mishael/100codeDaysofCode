numlist = [1, 2, 3]
numlist.reverse()

mystr = "Waad"
lst_str = list(mystr)

lst_str.pop()
"""returns the last letter from the list and remove it"""
"""and we can give pop an index"""
lst_str.insert(3, 'd')
del lst_str[0]

lst_str.append(2000)

# mutability (can be changed) and imutability (cant be changed)

dictonary = {"waad": 2000}
dictonary["Rawan"] = 1990

# just keys
dictonary.keys()
# just values
dictonary.values()
# all
dictonary.items()

# string %s
# digit %d
