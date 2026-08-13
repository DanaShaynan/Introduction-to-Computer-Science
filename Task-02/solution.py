# Find the maximum number and its location in an array

numbers = []

# Input 10 elements
for i in range(10):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

# Assume first element is maximum
maximum = numbers[0]
location = 0

# Search for maximum number
for i in range(1, 10):
    if numbers[i] > maximum:
        maximum = numbers[i]
        location = i

print("\nArray:")
print(numbers)

print("Largest number:", maximum)
print("Location:", location + 1)
