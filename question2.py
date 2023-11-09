def quick_sort(arr):
    less = []
    pivot = []
    more = []
    if len(arr) < 2:
        return arr
    else:
        for i in arr:
            if i < arr[0]:
                less.append(i)
            elif i < arr[0]:
                more.append(i)
            else:
                pivot.append(i)

    less = quick_sort(less)
    more = quick_sort(more)
    return less + pivot + more
