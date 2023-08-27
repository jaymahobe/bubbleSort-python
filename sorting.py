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
32, 77, 50, 11, 68, 28, 96, 53, 15, 82, 39, 75, 22, 61, 8, 47, 70, 17, 44,
89, 31, 64, 3, 56, 21, 78, 40, 74, 2, 87, 52, 18, 45, 80, 33, 66, 9, 48, 71,
26, 93, 16, 59, 34, 76, 12, 54, 85, 1, 46, 79, 29, 65, 4, 51, 24, 90, 7, 60,
35, 73, 13, 55, 86, 20, 38, 95, 62, 27, 94, 6, 41, 83, 37, 84, 98, 99, 97, 42 ]

# Call the bubble_sort function to sort the numbers
bubble_sort(numbers)

# Print the sorted numbers
print(numbers)
