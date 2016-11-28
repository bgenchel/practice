# Enter your code here. Read input from STDIN. Print output to STDOUT\


def print_array(array):
    print " ".join(map(str, array))


def swap(array, index1, index2):
    temp = array[index2]
    array[index2] = array[index1]
    array[index1] = temp


def quick_sort(array, left, right):
    if right - left < 1:
        return

    pivot = array[right]
    gt_index = left
    for i in xrange(left, right):
        if array[i] < pivot:
            # this conditional is an optimization not anticipated
            # by hacker rank
            if gt_index < i:
                swap(array, gt_index, i)
            gt_index += 1
    swap(array, gt_index, right)
    # print_array(array)

    quick_sort(array, left, gt_index - 1)
    quick_sort(array, gt_index + 1, right)

discard = raw_input()
arr = map(int, raw_input().split())
quick_sort(arr, 0, len(arr) - 1)
print_array(arr)
