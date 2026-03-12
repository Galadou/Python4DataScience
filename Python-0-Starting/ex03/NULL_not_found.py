

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: " + str(object) + " " + str(type(object)))
    elif type(object) is float and object != object:  # NaN is NaN return false
        print("Cheese: " + str(object) + " " + str(type(object)))
    elif object == 0 and type(object) is int:
        print("Zero: " + str(object) + " " + str(type(object)))
    elif object == "":
        print("Empty:" + str(object) + " " + str(type(object)))
    elif object is False:
        print("Fake: " + str(object) + " " + str(type(object)))
    else:
        print("Type not Found")
        return 1
    return 0
