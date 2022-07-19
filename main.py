

# quick sort

# Separates a large group of items to be sorted into smaller groups

# A pivotal item is chosen from the list (usually an item from the middle of the set)
# and is moved to the end of the list.
# From the left of the list, you go right until you reach an item that's smaller than the 
# pivot. From the right of the list (not including the pivot) you go left until you reach 
# an item smaller than the pivotal item, and you swap the positions of the left and right 
# items
# You go through all the numbers in the list until all of them have been compared
#
#
# If the pivot is chosen effectively, quick sort can be one of the more efficient sorting methods 

# a_list = [5, 3, 43, 76, 102, 45, 17, 13, 22, 19, 18, 1, 7, 99, 207]
'''
# /* low  --> Starting index,  high  --> Ending index */
quickSort(arr[5, 3, 43, 76, 102, 45, 17, 13, 22, 19, 18, 1, 7, 99, 207], low, high)
{
    if (low < high):
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
'''


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

#[5, 2, 3, 3, 5, 9 ,7, 10]
#[ 2, 3, 3, 5] [9 ,7, 10]
#              [7, 9]
#[2, 3, 3, 5, 5, 7, 9, 10]

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
# Driver code to test above
arr_1 = [10, 7, 8, 9, 1, 5]
my_arr = [-7, 5, 3, 43, 76, 102, 45, 17, 13, 22, 0, 19, 18, 1, 7, 99, 207]
arr = my_arr
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),