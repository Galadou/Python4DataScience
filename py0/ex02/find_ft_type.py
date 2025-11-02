

def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print("List : " + str(type(object)))
    elif type(object) == tuple:
        print("Tuple : " + str(type(object)))
    elif type(object) == set:
        print("Set : " + str(type(object)))
    elif type(object) == dict:
        print("Dict : " + str(type(object)))
    elif type(object) == str:
        print(object + " is in the kitchen : " + str(type(object)))
    else :
        print("Type not found")
    return 42