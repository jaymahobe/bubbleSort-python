def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
# this loop is check the 1st digit and 2nd digit which is greater (j+1 is not a adding thing it is for check the digits perticular way)
            if array[j] > array[j+1]:

                # this loop is for swapping
                array[j], array[j+1] = array[j+1], array[j]

# given number is 1 to 100
numbers = [ 8, 9, 4, 6, 1, 3, 2, 5, 7]

# Call the bubble_sort function to sort the numbers
bubble_sort(numbers)

# Print the sorted numbers
print(numbers)
