def minimunSwaps(A):
    swaps = 0
    N = len(A)

    for element_index in range(N):
        while A[element_index] - 1 != element_index:
            element = A[element_index]
            A[element_index], A[element] = A[element], A[element_index]
            swaps += 1
    return swaps

