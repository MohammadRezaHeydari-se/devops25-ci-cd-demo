def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a - b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
