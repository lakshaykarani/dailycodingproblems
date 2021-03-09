#!/usr/bin/env python3

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
'''
def sum_of_k(num_list: list, k: int) -> bool:



    for i, elem in enumerate(num_list):
        num_list.pop(i)
        if k-elem in num_list:
            return True
            
        num_list.insert(i,elem)
    return False 

if __name__ == "__main__":
    
    num_list = [10, 15, 3, 7]
    k = 14

    print(sum_of_k(num_list,k))