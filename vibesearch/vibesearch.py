def vibesearch(data, target):
    """
    A fun, vibe-based searching algorithm.
    Not guaranteed to work logically. Just for fun.
    """
    matches = [str(index) for index, value in enumerate(data) if value == target]

    if matches:
        return ", ".join(matches)

    return None
