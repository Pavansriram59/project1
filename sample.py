#generate code for power of a number
def power(base, exponent):
    """Calculate the power of a number.

    Args:
        base (float): The base number.
        exponent (int): The exponent to raise the base to.

    Returns:
        float: The result of base raised to the power of exponent.
    """
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1 / result
    return result
# Example usage
if __name__ == "__main__":
    print(power(2, 3))      # Output: