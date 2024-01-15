l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def add_two_numbers(l1, l2):
    '''Add'''

    upper_list, lower_list = [l1, l2] if len(l1) > len(l2) else [l2, l1]

    new_array = []

    lower_list =  ( [0] * (len(upper_list) - len(lower_list)) ) + lower_list
    current_numarator = 0

    # for item1, item2 in zip(upper_list, lower_list):
    for i in range(len(upper_list)- 1, -1, -1):

        sum = upper_list[i] + lower_list[i] + current_numarator
        numarator , demarator = sum // 10, sum % 10

        new_array.append(demarator)

        current_numarator = numarator

    if current_numarator != 0:
        new_array.append(current_numarator)
        
    return new_array



print(add_two_numbers(l1 = [0], l2 = [0]))
