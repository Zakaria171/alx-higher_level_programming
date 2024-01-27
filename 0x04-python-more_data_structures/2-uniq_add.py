#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = my_list[0]
    for i in range(1, len(my_list)):
        sum_uniq = sum_uniq + my_list[i]
        for j in range(0, i - 1):
            if my_list[j] == my_list[i]:
                sum_uniq = sum_uniq - my_list[i]
                break
    return (sum_uniq)
