numbers = "1 2 7 4 -5"

def high_and_low(numbers):
    num_list_string = numbers.split()
    print (num_list_string)

    num_list_int = []
    for i in num_list_string:
        i = int(i)
        num_list_int.append(i)

    sorted_list = sorted(num_list_int)
    print(sorted_list)

    numbers = '{} {}'.format(sorted_list[len(sorted_list)-1], sorted_list[0])
    return numbers

print(high_and_low(numbers))
