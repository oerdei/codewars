def set_alarm(employed, vacation):
    if employed is True and vacation is False:
        return True
    return False
employed = False
vacation = False
print(set_alarm(employed, vacation))