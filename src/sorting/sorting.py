# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(a, b):
    elements = len(a) + len(b)
    # merged_arr = [0] * elements

    # Your code here:

    # empty sorted array
    sorted = []
    ai = 0
    bi = 0

    while len(sorted) < elements:
        if ai >= len(a):
            sorted.append(b[bi])
            bi += 1
        elif bi >= len(b):
            sorted.append(a[ai])
            ai += 1
        elif a[ai] < b[bi]:
            sorted.append(a[ai])
            ai += 1
        elif a[ai] >= b[bi]:
            sorted.append(b[bi])
            bi += 1
    return sorted


# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here:

    # check if empty array
    if len(arr) == 0:
        return []

    # Base Case

    # divide array by middle index
    middle = len(arr) // 2

    # Store Left and Right array
    LHS = arr[:middle]
    RHS = arr[middle:]

    # Recursive
    if len(arr) > 1:
        LHS = merge_sort(LHS)
        RHS = merge_sort(RHS)

    # return with merge helper function
    return merge(LHS, RHS)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


arr = [35, 12, 24, 16, 13, 1, 45, 3, 5]

print(merge_sort(arr))


# arr1 = [2, 3, 9, 21]
# arr2 = [1, 5, 20, 7]

# arr1 = [2, 3, 5, 22]
# arr2 = [1, 4, 20]

# merge(arr1, arr2)
