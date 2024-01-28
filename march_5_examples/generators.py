"""Generator examples."""

def awesome_range(start, end, step=1):
    """
    Creates an awesome range.

    start - int
    end - int
    step - int (optional)
    """
    current_value = start
    while current_value < end:
        yield current_value
        current_value += step
