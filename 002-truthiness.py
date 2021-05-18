# Data Science from Scratch by Joel Grus

# all takes an iterable and returns True if all values are Truthy
print(all([True, 1, []]))  # False since [] is Falsy

# any takes an iterable and returns True if any values are Truthy
print(any([False, [], 1]))

x = None
# always return a number
safe_x = x or 0
print(safe_x)
# alternative
safe_x = x if x is not None else 0
print(safe_x)
