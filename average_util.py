def average(*args):
    """
    Computes the arithmetic mean of the provided arguments.
    Supports individual numbers or a single list/tuple.
    """
    # If the first argument is a list or tuple, use that
    if len(args) == 1 and hasattr(args[0], '__iter__'):
        data = args[0]
    else:
        data = args
        
    if not data:
        raise ValueError("At least one number is required to compute the average.")
    
    # Using a list to support generators/iterables
    values = list(data)
    return sum(values) / len(values)

# Example usage
print(average(10, 20, 30))