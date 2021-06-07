def reverseArray(A):
    index = len(A)
    for item_index in range(index//2):
        swappable_index = index - item_index - 1
        A[item_index], A[swappable_index] = A[swappable_index], A[item_index]
    return A

print(reverseArray([1,2,3,4]))
print(reverseArray([10,5,6,9]))
print(reverseArray([4,3,2,1,9,6,5,10]))
