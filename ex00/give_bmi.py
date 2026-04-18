def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Returns a list of body mass indexes from lists of height and weight"""
    if len(height) != len(weight):
        raise ValueError("Les listes doivent avoir la meme taille")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError(
                "Les listes doivent contenir uniquement des int ou float"
                )
        if h <= 0 or w <= 0:
            raise ValueError("Wrong value")

    return [a / (b * b) for a, b in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of boolean values representing the result
    of comparing the limit to the list."""
    if not isinstance(limit, int):
        raise ValueError("Wrong value")

    for v in bmi:
        if not isinstance(v, (int, float)):
            raise ValueError("Wrong value in list")
    return [a > limit for a in bmi]
