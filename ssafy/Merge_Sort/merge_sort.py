in_arr = [9, 6, 3, 1, 10, 4, 8, 15, 2, 11, 244, 6345, 2, 14, 2, 3, 1, 325, 232, 1]


def merge_sort(arr, n):
    if n == 1: return arr

    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    sorted_left_arr = merge_sort(left_arr, len(left_arr))
    sorted_right_arr = merge_sort(right_arr, len(right_arr))

    for i in range(len(arr)):
        if len(sorted_left_arr) == 0:
            arr[i] = sorted_right_arr.pop(0)
        elif len(sorted_right_arr) == 0:
            arr[i] = sorted_left_arr.pop(0)
        elif sorted_left_arr[0] < sorted_right_arr[0]:
            arr[i] = sorted_left_arr.pop(0)
        else:
            arr[i] = sorted_right_arr.pop(0)
    return arr


print(in_arr)
out_arr = merge_sort(in_arr, len(in_arr))
print(out_arr)