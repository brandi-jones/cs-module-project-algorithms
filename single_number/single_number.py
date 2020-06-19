'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#     singleNumber = None
    
#     for x in arr:
#         if arr.count(x) == 1:
#             singleNumber = x
            
#     return singleNumber

def single_number(arr):
    # keep track of number of times an item occurs in input
    # use a dictionary here, because searching through dicts on average has a time complexity of O(1) vs O(n) of an array
    counts = {}

    # loop through input list O(n)
    for item in arr:
        # if item in counts
        if item in counts:
            # remove item
            del counts[item]
        # otherwise
        else:
            counts[item] = 1
            # add item

    for k, v in counts.items(): # O(1)
        if v == 1:
            return k
            


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")