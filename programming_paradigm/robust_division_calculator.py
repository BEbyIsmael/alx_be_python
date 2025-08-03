def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric input.
    Args:
        numerator: The numerator value (expected to be convertible to float).
        denominator: The denominator value (expected to be convertible to float).
    Returns:
        str or float: The result of the division, or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        try:
            result = num / denom
            return print(f"The result of the division is {result}")
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
