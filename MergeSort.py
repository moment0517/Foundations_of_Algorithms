def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    arr_p1 = merge_sort(arr[:mid])
    arr_p2 = merge_sort(arr[mid:])

    len1 = len(arr_p1)
    len2 = len(arr_p2)
    if len1 == 0:
        return arr_p2
    elif len2 == 0:
        return arr_p1
    else:
        res = []
        i1 = 0
        i2 = 0
        while i1 < len1 and i2 < len2:
            if arr_p1[i1] < arr_p2[i2]:
                res.append(arr_p1[i1])
                i1 += 1
            else:
                res.append(arr_p2[i2])
                i2 += 1
        if i1 == len1:
            while i2 < len2:
                res.append(arr_p2[i2])
                i2 += 1
        else:
            while i1 < len1:
                res.append(arr_p1[i1])
                i1 += 1

        return res
