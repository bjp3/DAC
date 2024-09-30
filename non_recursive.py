
def non_recursive(array):
    max_sum = float('-inf')  # establishes the sum as negative infinity if there's an all negative array
    n = len(array) # establishes the length of the array
    start = 0
    end = 0

    for i in range(n):
        for j in range(i,n):
            current_sum = sum(array[i:j + 1])
            if current_sum > max_sum:
                max_sum = current_sum
                start = array[i]
                end = array[j]
                x = i
                y = j
    return f'i = {start}, i index = {x}\nj = {end}, j index = {y}\nMax Sum = {max_sum}'
