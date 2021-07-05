def merge(low, mid, high):
    i = low
    j = mid+1
    k = low
    b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while i <= mid and j <= high:
        if nums[i] > nums[j]:
            b[k] = (nums[j])
            j += 1
        else:
            b[k] = (nums[i])
            i += 1
        k += 1

    if i <= mid:
        while i != mid+1:
            b[k] = (nums[i])
            i += 1
            k += 1

    elif j <= high:
        while j != high + 1:
            b[k]=(nums[j])
            j += 1
            k += 1
    for k in range(low, high+1):
        nums[k] = b[k]


def merge_sort(low, high):

    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid+1, high)
        merge(low, mid, high)
    return

nums = [5,4,0,2,1,1,2,15,4,4,4,00]
merge_sort(0, len(nums)-1)
print(nums)


