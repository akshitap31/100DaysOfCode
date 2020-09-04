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

# def twoSum(nums, target):
#     for i in nums:
#         if (target - i) in nums:
#             return print([nums.index(i), nums.index(target - i)])
#             break
# twoSum([2,7,11,15],9)