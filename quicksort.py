nums = [5,4,0,2,1,1,2,15,4,4,4,00]


def partition(low, high):
    i = low-1
    j = high+1
    pivot = low

    while i < j:
        while True:
            i += 1
            if i == high or nums[i] > nums[pivot]:
                break
        while True:
            j -= 1
            if nums[j] < nums[pivot] or j == low:
                break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[j], nums[pivot] = nums[pivot], nums[j]
    return j


def quicksort(low, high):
    if low < high:
        j = partition(low, high)

        quicksort(low, j)
        quicksort(j+1, high)


quicksort(0, len(nums)-1)
print(nums)
