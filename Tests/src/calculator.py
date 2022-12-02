def sum_values(x, y):
    """
    Soma

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa der int ou float
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
