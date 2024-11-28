def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]
    max_val = max(arr)
    size = max_val / len(arr)

    for num in arr:
        index = int(num / size)
        if index != len(arr):
            bucket[index].append(num)
        else:
            bucket[len(arr) - 1].append(num)

    for i in range(len(arr)):
        bucket[i].sort(reverse=True)

    sorted_arr = []
    for sublist in bucket:
        sorted_arr.extend(sublist)

    return sorted_arr

weights = [70, 56, 45, 92, 81, 67]
print(bucket_sort(weights))
