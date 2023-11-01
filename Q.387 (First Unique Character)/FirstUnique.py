def character_check(my_dictionary,my_set,c,index):
    if c not in my_set:
        if c not in my_dictionary:
            my_dictionary[c] = index
        else:
            my_dictionary.pop(c)
            my_set.add(c)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        size = len(s)
        my_set = {-1}
        my_dictionary = {}
        for i in range(size):
            character_check(my_dictionary,my_set,s[i],i)

        if my_dictionary == {}:
            return -1
        else:
            return list(my_dictionary.values())[0]

        # dictionary that stores the first index of evey unique character
        # set that stores every duplicate character
        # after finding out that the element is in dictionary, we remove it from the dictionary and add the value inside the duplicate
        #the function begins everytime by checking if the character exists in the set to prevent adding and removing the character again to the dictionary