def renamer(name):
    name = name.split(", ")
    name[0] = name[0].replace(" ", "%20")
    final_name = name[1] + "--" + name[0]
    return final_name
