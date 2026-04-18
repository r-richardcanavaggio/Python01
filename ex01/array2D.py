def slice_me(family: list, start: int, end: int) -> list:
    """Prints shape of 2D array and slices it based on start/end indexes"""
    if (not isinstance(family, list)
            or not isinstance(start, int)
            or not isinstance(end, int)):
        raise ValueError("bad argument")
    elif not family:
        raise ValueError("empty list")
    elif not isinstance(family[0], list):
        raise ValueError("bad argument")
    print(f"My shape is ({len(family)}, {len(family[0])})")

    sliced = family[start:end]

    if not sliced:
        raise ValueError("empty sliced list")

    print(f"My new shape is ({len(sliced)}, {len(sliced[0])})")

    return sliced
