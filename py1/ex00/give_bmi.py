import numpy as np

# all = si un des bloc de la l'iterable est false alors false.
# Il faut quils soit tous vrais pour true.
# any = Si un bloc est true dedans, alors true.




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
