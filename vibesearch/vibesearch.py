def vibesearch(data, target):
    """
    A fun, vibe-based searching algorithm.
    Not guaranteed to work logically. Just for fun.
    """
    for index, value in enumerate(data):
        if value == target:
            return index  

    return None
