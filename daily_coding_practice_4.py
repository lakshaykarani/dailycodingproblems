'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

def lowest(num_list: list) -> int:

    for i in range(1,max(num_list)+2):
        if i not in num_list: return i

if __name__ == '__main__':
    print(lowest([1, 2, 0 ,6,8]))