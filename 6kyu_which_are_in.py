#
# def in_array(array1, array2):
#     new_arr = []
#     for word in array1:
#         if word in array2:
#             new_arr.append(word)
#     return new_arr
#
#
# print(in_array(["arp", "live", "strong"],
# ["lively", "alive", "harp", "sharp", "strong"]))
#
#
# array1 = ["arp", "live", "strong"]
# array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# #words
# char_list = []
#
# for word in array:
#
#     print(word)
#     for char in word:
#         print(char)
#         char_list.append(char)
#
#         #for i in range(0, len(word)):
# print(char_list)



# def new_word_list_func(array):
#     new_word = ''
#     new_word_list = []
#     for word in array:
#         #print(word)
#         for i in range(0,len(word)):
#             new_word = new_word + word[i]
#             new_word_list.append(new_word)
#             #print(new_word_list)
#             if new_word == word:
#                 new_word = ''
#     return new_word_list

# print(new_word_list_func(array2))

'''----------------------------------------------------------------------'''

# array1 = ["arp", "live", "strong"]
# array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# new_word_list = []
# new_arr = []
#
# def new_word_list_func(array):
#     new_word = ''
#     for word in array:
#         for starting_point in range(0,len(word)):
#             for i in range(starting_point,len(word)):
#                 new_word = new_word + word[i]
#                 new_word_list.append(new_word)
#                 #print(new_word_list)
#                 if new_word[len(new_word)-1] == word[len(word)-1]:
#                     new_word = ''
#     return new_word_list
#
# new_word_list_func(array2)
#
# def in_array(array1, array2):
#
#     for word in array1:
#         if word in new_word_list:
#             new_arr.append(word)
#     return new_arr
#
#
# print(in_array(array1, array2))

'''my solution ----------------------------------------------------------------------'''
array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    new_word_list = [] #creating a new_word_list to be compared with array1
    new_word = '' #initializing empty string of each word to be stored in new_word_list
    for word in array2:
        for starting_point in range(0,len(word)): #creating a starting_point for every char in the particular word in array2
            for i in range(starting_point,len(word)): #starting to iterate through every char in the particular word
                new_word = new_word + word[i] # adding every char to its previous char
                new_word_list.append(new_word)
                #print(new_word_list)
                if new_word[len(new_word)-1] == word[len(word)-1]:
                #when last char of new word is equal to the last char of the word angain initialize a empty string
                #to avoid other words of array2 to mix with new_word and execute seperately
                    new_word = ''


    new_arr = []
    for word in array1:
        if word in new_word_list:
            new_arr.append(word)
    return sorted(list(set(new_arr)))
    #set for removing duplicates
    #convert set to list
    #sort out list

print(in_array(array1, array2))


'''cheznuggets solution ----------------------------------------------------------------------'''
def in_array(array1, array2):
    array3 = []
    for substr in array1:
        for word in array2:
            if substr in word and substr not in array3:
                array3.append(substr)
                break
    return sorted(array3)

print(in_array(array1, array2))
