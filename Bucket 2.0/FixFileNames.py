def Fixer(name) : #

    name = name.replace(".bk", "")

    index = name.rfind("\\")

    name = name[index + 1:]

    return name
#