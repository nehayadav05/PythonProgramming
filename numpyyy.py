import numpy as np

# Create a 2D array of zeros with 3 rows and 4 columns
my_array = np.zeros((3, 4))

# Print the array
print(my_array)

# Set the value of the first element in the first row to 1
my_array[0, 0] = 1

# Print the modified array
print(my_array)

# Compute the sum of all elements in the array
total_sum = np.sum(my_array)

# Print the total sum
print(total_sum)
