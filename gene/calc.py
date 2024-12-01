
def add(x, y: int) -> int:
    """add fucntion takes two integers and return the addition of those numbers."""
    return x + y


def subtract(x, y: int) -> int:
    """subtract function takes two integers and return the subtraction of those numbers."""
    return x - y


def multiply(x, y: int) -> int:
    """multiply function takes two integers and return the multiplication of those numbers."""
    return x * y


def divide(x, y: int) -> int:
    """divide function takes two integers and return the division of those numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
