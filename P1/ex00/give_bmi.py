def give_bmi(height: list[int | float], weight: list[int | float]):
    """Give the BMI of a list of height and weight"""
    assert len(height) == len(weight), "Array are not the same size."
    assert all(
        isinstance(x, int) or isinstance(x, float) for x in height
        ), "List can contains only int or float"
    assert all(
        isinstance(x, int) or isinstance(x, float) for x in weight
        ), "List can contains only int or float"
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / height[i] ** 2)
    return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list that contains True or False \
if the BMI is over the limit"""
    assert bmi, "Impossible to apply limit on empty array."
    is_whale = [True if item > limit else False for item in bmi]
    return is_whale
