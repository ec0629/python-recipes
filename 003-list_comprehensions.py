# Data Science from Scratch by Joel Grus

inp = [99, 101, 34, 0, -32]

only_positive_values = [i for i in inp if i >= 0]
print(only_positive_values)

with_default_values = [i if i >= 0 else 0 for i in inp]
print(with_default_values)

# using multiple fors
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]
print(pairs)

# earlier values in the for statements cascade to later for statements
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
print(increasing_pairs)


# Create other collection types
square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(square_dict)
square_set = {x * x for x in [1, -1]}  # {1}
print(square_set)

# creating from two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

pairs = [pair for pair in zip(list1, list2)]
print(pairs)

# unpacking tuples
letters, numbers = zip(*pairs)
print(letters)
print(numbers)
