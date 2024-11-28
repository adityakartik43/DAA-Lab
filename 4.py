def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

arr = [1, 4, 2, 8, 5, 7, 6, 3, 10, 9]
print(counting_sort(arr, 10))
