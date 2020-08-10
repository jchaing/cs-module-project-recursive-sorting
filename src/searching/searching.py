# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # Check if start is greater than end
    if start > end:
        return -1

    else:
        # store middle index
        middle = (start + end) // 2

        # store guess
        guess = arr[middle]

        # if guess is the target, return the index
        if guess == target:
            print(guess)
            return middle

        # if target is greater than guess, recursive search right half
        elif target > guess:
            return binary_search(arr, target, (middle + 1), end)

        # if target is less than guess, recursive search left half
        else:
            return binary_search(arr, target, start, (middle - 1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass


arr = [1, 2, 3, 4, 5]
binary_search(arr, 3, 0, len(arr) - 1)

