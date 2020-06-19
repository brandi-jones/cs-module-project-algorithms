'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     #base cases
#     #when there are no more cookies to eat
#     if n == 0:
#         return 1

#     if n < 0:
#         return 0

#     #option to eat 1, 2, or 3 cookies
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, cache=None):
    #base cases
    #when there are no more cookies to eat
    if n == 0:
        return 1

    if n < 0:
        return 0
    
    if cache is None:
        cache = {}

    #if we have already seen this iteration before
    if n in cache:
        return cache[n]

    #option to eat 1, 2, or 3 cookies
    return eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
