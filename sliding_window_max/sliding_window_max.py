'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    maxNums = []
    index, end = 0, len(nums)
    
    while index + k <= end:
        maxNums.append(max(nums[index:index + k]))
        index+=1

    return maxNums
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    arr = [1, 2, 5, 7, 5, 9] #answer should be [5, 7, 7, 9]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
