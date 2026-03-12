import numpy as np

# all = si un des bloc de la l'iterable est false alors false.
# Il faut quils soit tous vrais pour true.
# any = Si un bloc est true dedans, alors true.


def give_bmi(height: list[int | float], weight: list[int | float]) \
      -> list[int | float]:
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
