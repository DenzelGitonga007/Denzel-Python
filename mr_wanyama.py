"""Given two arrays with same length. 
Swap the elements of the even indices of the first array with those of the second, 
and vice versa"""


# Create the arrays
arr1 = []
arr2 = []
# Get the array length
arr_len = input("How many numbers do you want to have in one array? ")

# Append the numbers onto the first array
def array1():
    """ Get the numbers to add into the first array """
    print("Enter the numbers for the first array: ")
    for i in range(0, int(arr_len)):
        arr1_nums = int(input())
        arr1.append(arr1_nums)

    print("The first array has the numbers: {}".format(arr1))

# Append the numbers onto the second array
def array2():
    """ Get the numbers to add into the second array """
    print("Enter the numbers for the second array: ")
    for i in range(0, int(arr_len)):
        arr2_nums = int(input())
        arr2.append(arr2_nums)

    print("The second array has the numbers: {}".format(arr2))

# Swapping the numbers of the even indices
def swap():
    """ Swap the numbers of even indices """
    for index, value in enumerate(arr1):
        if index % 2 == 0:
            # remove the values, and put into arr2
        

array1()
array2()
swap()