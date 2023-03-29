import random
import time


# naive search: scan entire list and ask if its equal to target
# If yes, return the index
# If no, then return -1
def naive_search(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1


# binary search: divide and conquer.
# Works only in sorted lists
# If yes, return the index
# If no, then return -1
def binary_search(arr, x):
    """
    Searches for the value x in the sorted array arr using binary search.
    Returns the index of x in the array if found, else returns -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""
This function takes in two arguments: an array arr that is assumed to be sorted in ascending order, and a value x that we want to search for in the array. The function returns the index of x in the array if found, or -1 if x is not in the array.

The function first initializes left and right variables to represent the left and right boundaries of the subarray we're searching in. We then enter a while loop that continues as long as left is less than or equal to right. At each iteration of the loop, we calculate the middle index mid of the subarray and check if the value at mid is equal to x. If it is, we return mid.

If arr[mid] is less than x, then we know that x can only be in the subarray to the right of mid, so we update left to be mid + 1. If arr[mid] is greater than x, then we know that x can only be in the subarray to the left of mid, so we update right to be mid - 1.

If we exit the while loop without finding x, then we know that x is not in the array and we return -1.
"""


if __name__ == "__main__":

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for x in sorted_list:
        naive_search(sorted_list, x)
    end = time.time()
    print(f"Naive search time: {end - start} seconds")

    start = time.time()
    for x in sorted_list:
        binary_search(sorted_list, x)
    end = time.time()
    print(f"Binary search time: {end - start} seconds")
