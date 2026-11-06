def addition(a, b):
    """Return the sum of two values.

    Args:
        a: The first addend (number or any value supporting ``+``).
        b: The second addend, of a compatible type with ``a``.

    Returns:
        The result of ``a + b``.

    Example:
        >>> addition(2, 3)
        5
    """
    return a + b

if __name__ == "__main__":
    print(addition(20, 30))
