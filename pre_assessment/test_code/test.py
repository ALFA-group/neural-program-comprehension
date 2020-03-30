def find_lowest(lst):
    # Return the lowest positive number in a list.
    def lowest(first, rest):
        # Base case
        if len(rest) == 0:
            print(first) # This line is only to check the value
            return first
        if first > rest[0] or first < 0:
            return lowest(rest[0], rest[1:])
        else:
            return lowest(first, rest)
    return lowest(lst[0], lst[1:])

a = [6, 6, 6, 6, 6]
print(find_lowest(a)) # Prints None, but should print the lowest number