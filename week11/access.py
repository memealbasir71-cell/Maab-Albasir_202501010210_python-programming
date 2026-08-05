def check_access(registered, lab_open, computer_available):

    if registered == "Y" and lab_open == "Y" and computer_available == "Y":
        return "access granted"
    else:
        return "access deniad"

def get_reason(registered, lab_open, computer_available):

    if registered != "Y":
        return "student is not registerd"
    elif lab_open != "Y":
        return "computer lab is closed"
    elif computer_available != "Y":
        return " no available computer"
    else:
        return "welcome to lab"