'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    
    y = len(arr)-1
    for x in range(0, len(arr)-1):
        while arr[x] == 0:
            if arr[y] != 0:
                #swap
                arr[x], arr[y] = arr[y], arr[x]
            #if x and y are at the same index, return
            elif x == y:
                return arr
            else:
                #subtract 1 from y index to move to the next right most position which is unknown if it is a 0 or not
                y-=1
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")