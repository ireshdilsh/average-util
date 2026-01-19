# This function computes the average of a variable number of numerical arguments.
def average(*args):
  # check arguments is provided
 if not args:
    #  raise an error if no arguments are provided
    raise ValueError("At least one number is required to compute the average.")
  # return the average of the provided numbers
 return sum(args) / len(args)

# Example usage
print(average(10, 20, 30))