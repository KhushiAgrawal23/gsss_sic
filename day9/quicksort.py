from partition2 import partition_array as pa

def quick_sort(array, low, high):
    if high > low:
        pivot_index = pa(array, low, high)
        # generate_image(array, pivot_index)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index+1, high)

l1 = [34, 223, 22, 31, 1, 100, 50, 40, 22, 72]
print(f'Before Sorting: {l1}')
quick_sort(l1, 0, len(l1)-1)
print(f'After Sorting: {l1}')