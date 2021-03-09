'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def product_list(num_list: list) -> list:

    op = []
    prod = 1
    for i, elem in enumerate(num_list):
        num_list.pop(i)
        for j in num_list:
            prod *= j
        op.append(prod)
        num_list.insert(i,elem)
        prod=1
    return op
if __name__ == "__main__":

    print(product_list([1, 2, 3, 4, 5]))
    print(product_list([3,2,1]))