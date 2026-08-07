def get_sorted_list(numbers):
    """Sorts a list of numbers in ascending order and returns it."""
    # INTENTIONAL BUG: .sort() modifies the list in place and returns 'None'
    # It should be: return sorted(numbers) OR numbers.sort() then return numbers
    return numbers.sort()