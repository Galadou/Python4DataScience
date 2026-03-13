import numpy as np

# all = If one of the blocks in the iterable is false, then false.
# They must all be true for it to be true.
# any = If a block is true within it, then true.


def give_bmi(height: list[int | float], weight: list[int | float]) \
      -> list[int | float]:
    """
    Take a list of heights and a list of weights \
        And return a list of the bmi calculated with these 2 params.

    Args:
        height (list[int | float]): A list of height.
        weight (list[int | float]): A list of weight.
    Returns:
        list[int | float]: A list of bmi based on height and weight.
    """
    try:
        if not isinstance(height, list) \
                or not all(isinstance(i, (int, float)) for i in height):
            raise AssertionError("height should take only integer or float.")
        if not isinstance(weight, list) \
                or not all(isinstance(i, (int, float)) for i in weight):
            raise AssertionError("weight should take only integer or float.")
        if len(height) != len(weight):
            raise AssertionError("weight and height have not the same size.")
        np_height = np.array(height)
        np_weight = np.array(weight)
        if any(i <= 0 for i in np_height):
            raise AssertionError("height cannot be negative or equal to 0.")
        if any(i <= 0 for i in np_weight):
            raise AssertionError("weight cannot be negative or equal to 0.")
        bmi_result = np_weight / (np_height ** 2)
        result = bmi_result.tolist()
        return result
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")
    return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Take a list of bmi, and a limit as int.
    Return a list of bool that says if the value in bmi is above the limit.

    Args:
        bmi (list[int | float]): A list of bmi.
        limit (int): A limit number.
    Returns:
        list[bool]: A list of boolean based on the bmi list,\
             true if above the limit.
    """
    try:
        if not isinstance(bmi, list) \
                or not all(isinstance(i, (int, float)) for i in bmi):
            raise AssertionError("bmi should take only integer or float.")
        np_bmi = np.array(bmi)
        result = np_bmi > limit
        return result.tolist()
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")
    return None
