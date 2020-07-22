def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    arr_p1 = []
    arr_p2 = []
    for i in range(1, len(arr)):
        item = arr[i]
        if item <= pivot:
            arr_p1.append(item)
        else:
            arr_p2.append(item)
    arr_p1 = quick_sort(arr_p1)
    arr_p2 = quick_sort(arr_p2)

    return arr_p1 + [pivot] + arr_p2
