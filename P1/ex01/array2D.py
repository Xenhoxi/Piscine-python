import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert all(
        isinstance(x, list) for x in family
        ), "Arguments have to be type"
    array = np.array(family)
    new_array = array[start:end]
    print(f"My shape is : {array.shape}")
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
