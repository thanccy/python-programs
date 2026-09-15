numbers = input("Enter comma-separated numbers: ")

# Create list
num_list = numbers.split(',')

# Create tuple
num_tuple = tuple(num_list)

# Display results
print("Generated List:", num_list)
print("Generated Tuple:", num_tuple)
print("Total number of elements:", len(num_list))
print("First element:", num_list[0])
print("Last element:", num_list[-1])
print("List in reverse order:", num_list[::-1])