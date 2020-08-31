#Two nums
def two_nums(list, target):
    # iter through each number of list
    for i in list:
    # reduce num from target
    # check if balancing is in the list
    # if found, exit loop
        if (target - i) in list:
            return print([list.index(i), list.index(target-i)])
            break
    # return index
two_nums([1,2,3,4,5,6],11)