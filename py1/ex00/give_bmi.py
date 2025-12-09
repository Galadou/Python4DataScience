

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if type(height) is not int and type(height) is not float:
            raise AssertionError("height should take only integer or float.")
        if type(weight) is not int and type(weight) is not float:
            raise AssertionError("weight should take only integer or float.")
        if len(height) != len(weight):
            raise AssertionError("weight and height should have the same size.")
    except Exception as error:
        print(f"{type(error)} : {error}")

    

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

