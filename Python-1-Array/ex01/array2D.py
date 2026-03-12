import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    try:
        if not (isinstance(family, list)):
            raise AssertionError("family is not a list.")
        if (len(family) == 0):
            raise AssertionError("family cannot be empty.")
        if not (all(len(x) == len(family[0]) for x in family)):
            raise AssertionError("Mismatched family's argument sizes.")

        np_list = np.array(family)
        print(f"My shape is : {np_list.shape}")

        # start : stop : step
        np_list_sliced = np_list[start: end]

        print(f"My new shape is : {np_list_sliced.shape}")
        result = np_list_sliced.tolist()
        return result

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"{type(error)} : {error}")
