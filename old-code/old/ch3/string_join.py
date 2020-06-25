def string_join(lst):
    builder = ""
    for index, value in enumerate(lst):
        if index == 0:
            builder += str(value)
        else:
            builder += "," + str(value)
    return builder
