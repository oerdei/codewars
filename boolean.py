def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

name = "rOtto"
print(are_you_playing_banjo(name))

