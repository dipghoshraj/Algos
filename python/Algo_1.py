''' Write an algorithm to produce the first 15 numbers of this series: 1,1,2,3,5,8,13,21…'''

''' 
*** mathematical equation > resp = n + (n+1) where n = index number

* Initial the index value with 0
* Set function defination
* add index with (index+1)
* interate this function for 15 times

*** Algorithm is n = index_value(n-1) + index_value(n-2) ***
'''


sequence_lis = []

for i in range(1, 15):
    if len(sequence_lis) >= 2:
        current_value = sequence_lis[-2:]
        current_value = current_value[0] + current_value[1]
        sequence_lis.append(current_value)
    else:
        sequence_lis.append(1)

sequence_lis = [str(x) for x in sequence_lis]
print(', '.join(sequence_lis))

