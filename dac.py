def max_crossing_sum(array, left, mid, right):
    left_sum = float('-inf')
    total = 0
    max_left = mid

    for i in range(mid, left - 1, -1):
        total += array[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1

    for i in range(mid + 1, right + 1):
        total += array[i]
        if total > right_sum:
            right_sum = total
            max_right = i
    return left_sum + right_sum, max_left, max_right

def max_subarray_sum_dac(array, left, right):

    if left == right:  # test for only one element
        return array[left], left, right

    mid = (left + right) // 2      # find the middle point

    # find the maximum subarray sum in the left half, right half, and crossing the mid this will send the
    # values back through the method.
    left_sum, left_i, left_j = max_subarray_sum_dac(array, left, mid)
    right_sum, right_i, right_j = max_subarray_sum_dac(array, mid + 1, right)
    cross_sum, cross_i, cross_j = max_crossing_sum(array, left, mid, right)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_i, left_j
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_i, right_j
    else:
        return cross_sum, cross_i, cross_j