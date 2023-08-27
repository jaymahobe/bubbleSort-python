def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
# this loop is check the 1st digit and 2nd digit which is greater (j+1 is not a adding thing it is for check the digits perticular way)
            if array[j] > array[j+1]:

                # this loop is for swapping
                array[j], array[j+1] = array[j+1], array[j]

# given number is 1 to 100
numbers = [ 67, 23, 91, 14, 58, 36, 72, 49, 81, 30, 10, 57, 88, 43, 69, 25, 92, 19, 63, 5,
32, 77, 50, 11, 68, 28, 96, 53, 15, 82, 39, 75]

# Call the bubble_sort function to sort the numbers
bubble_sort(numbers)

# Print the sorted numbers
print(numbers)
