from non_recursive import *
from dac import *
import time

def main():
    pos_array = [60, 100, 58, 3, 51, 71, 99, 34, 70, 95, 45, 31, -58, 57, 1000000, 83, 73, -12, 39, 89, 20, 88, 66, 19, 33, 52, 22, 32, 48, 17]
    neg_array = [-61, -11, -26, -57, -16, -42, -63, -61, -14, -40, -60, -72, -93, -75, -18, -92, -10, -3, -57, -35, -62, -59, -88, -21, -30, -11, -42, -33, -84, -13]
    mix_array = [-24, 97, 70, -37, 87, -7, 89, 20, -46, -60, -17, -74, 13, -3, 7800, 3, 60, 6, 62, -94, 29, -41, -18, -32, -75, 62, 46, -14, -75, 94]
    single_array = [83]
    large_array = [46, -62, 53, 24, -4, 84, 68, 57, 62, 15, 26, 5, -29, -87, 76, -19, -76, 30, 21, 91, 39, -59, -33, -70, -83, -16, 87, 34, 24, -88, -3, 86, -80, 50, -94, 52, 14, -67, -1, 56, 75, 17, -81, -42, -20, -45, -7, 34, -66, 96, 87, -66, -18, 88, -58, 71, -31, -8, 63, 50, -13, 10, 16, 49, 98, -17, 48, -80, 55, -11, 70, -58, -80, 79, 81, 22, -1, -92, 62, -83, -89, -68, 66, 56, 34, -82, -85, 39, 92, 91, -59, -1, 67, -42, -83, -58, 99, 87, -21, 13, -10, -42, 53, 63, -57, -89, 86, 98, -58, 41, 67, -50, 92, -50, -78, 4, 82, 43, 85, 60, 30, 51, 96, -7, 42, -72, -35, -41, 91, 65, 62, -11, -84, 7, 74, 78, -5, -17, -86, -37, -77, -19, -84, -41, 16, -58, -94, -29, -8, -94, 1000000, -39, -93, -7, 36, -17, -77, 35, -49, -29, 9, 63, 100, -88, -15, 93, -56, 19, 80, 30, 65, -82, 63, 50, -39, 27, 25, -52, 84, -89, 18, 54, 33, -8, 2, -13, -1, -78, -64, -22, 5, -33, 98, -29, -28, 0, 72, -72, -52, 23, -19, -51, 50, -21, -47, 34, -61, 14, 12, -34, 49, -78, -69, 38, 1, -18, -16, -39, -2, 93, 23, 39, -2, 16, 21, 15, 76, -8, 54, 21, 98, -50, -53, -79, -82, -60, 4, -98, -98, -59, -100, -8, 40, -76, -34, -86, -17, -76, -32, 62, -83, -63, -47, 92, -90, 10, 43, -2, 27, 100, -10, 92, -29, -15, -16, 0, -42, 87, -48, 36, -64, 98, 66, 65, 96, 37, -16, -38, 87, 23, 20, -1, 31, -20, 53, 84, 71, 94, 37, -84, -65, -44, 81, -11, -89, -80, 39, -98, 45, -56]
    nr_start_time = time.time()
    print("Non-Recursive Results")
    pos_start_time = time.time()
    print(f'Positive Array:\n{non_recursive(pos_array)}')
    pos_end_time = time.time()
    print(f'Positive Array Time: {pos_end_time - pos_start_time}')
    neg_start_time = time.time()
    print(f'Negative Array:\n{non_recursive(neg_array)}')
    neg_end_time = time.time()
    print(f'Negative Array Time: {neg_end_time - neg_start_time}')
    mix_start_time = time.time()
    print(f'Mixed Array:\n{non_recursive(mix_array)}')
    mix_end_time = time.time()
    print(f'Mixed Array Time: {mix_end_time - mix_start_time}')
    single_start_time = time.time()
    print(f'Single Array:\n{non_recursive(single_array)}')
    single_end_time = time.time()
    print(f'Single Array Time: {single_end_time - single_start_time}')
    large_start_time = time.time()
    print(f'Large Array:\n{non_recursive(large_array)}')
    large_end_time = time.time()
    print(f'Large Array Time: {large_end_time - large_start_time}')
    print('-------------------------')
    nr_time = time.time() - nr_start_time
    print(f'Non-Recrusive Time: {nr_time}')
    r_new_start_time = time.time()
    print('Divide and Concur Recursive Results')
    print('-------------------------')
    r_pos_start_time = time.time()
    print(f'Positive Array:\n{max_subarray_sum_dac(pos_array, 0, len(pos_array) - 1)}')
    r_pos_end_time = time.time()
    print(f'Positive Array Time: {r_pos_end_time - r_pos_start_time}')
    r_neg_start_time = time.time()
    print(f'Negative Array:\n{max_subarray_sum_dac(neg_array, 0, len(neg_array) - 1)}')
    r_neg_end_time = time.time()
    print(f'Negative Array Time: {r_neg_end_time - r_neg_start_time}')
    r_mix_start_time = time.time()
    print(f'Mixed Array:\n{max_subarray_sum_dac(mix_array, 0, len(mix_array) - 1)}')
    r_mix_end_time = time.time()
    print(f'Mixed Array Time: {r_mix_end_time - r_mix_start_time}')
    r_single_start_time = time.time()
    print(f'Single Array:\n{max_subarray_sum_dac(single_array, 0, len(single_array) - 1)}')
    r_single_end_time = time.time()
    print(f'Single Array Time: {r_single_end_time - r_single_start_time}')
    r_large_start_time = time.time()
    print(f'Large Array:\n{max_subarray_sum_dac(large_array, 0, len(large_array) - 1)}')
    r_large_end_time = time.time()
    print(f'Large Array Time: {r_large_end_time - r_large_start_time}')
    print('--------------------------')
    dac_time = time.time() - r_new_start_time
    print(f'Divide and Conquer Time: {dac_time}')

if __name__ == '__main__':
    main()