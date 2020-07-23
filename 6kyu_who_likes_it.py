names = ["Max",'and', "John", "Mark",'and']
# names = ['a']
names = ["Max", "John", "Mark" , 'als']

print(names)

# names.insert(1,'1marc')
# names.insert(2,'2marc')
# names.insert(4,'3marc')
#
#
# print(names)
#
# for i in range(1,len(names)+2 , 2):
#     names.insert(i, 'and')
#
# names.insert(len(names)-1,'and')
# print(names)
#
# str = ' '.join(names) + ' likes this'
#
#
# print(str)
#
# empty_lst = ['sad']
# print(len(empty_lst))


# def likes(names):
#     names_list = []
#     for i in range(0,len(names)-1):
#         if names[i] == 'and':
#             del names[i]
#     print(names)
#
#
#     names_list = names[:]
#     print(len(names_list))
#
#     print (names_list)
#     if len(names_list) == 0:
#         str = "no one likes this"
#     elif len(names_list) == 1:
#         str = names_list[0] + ' likes this'
#     else:
#         for i in range(1,len(names_list)+2 , 2):
#             names_list.insert(i, 'and')
#
#         #names_list.insert(len(names_list)-1,'and')
#         #print(names)
#
#         str = ' '.join(names_list) + ' like this'
#     return str
#
# print(likes(names))






def likes(names):

    names_list = names[:]
    print(len(names_list))

    print (names_list)
    if len(names_list) == 0:
        string = "no one likes this"
    elif len(names_list) == 1:
        string = names_list[0] + ' likes this'
    elif len(names_list) == 2:
        string = '{} and {} like this'.format(names_list[0],names_list[1])
    elif len(names_list) == 3:
        string =  '{}, {} and {} like this'.format(names_list[0],names_list[1],names_list[2] )

    else:
        string =  '{}, {} and {} others like this'.format(names_list[0],names_list[1], len(names_list)-2)
    return string

print(likes(names))
