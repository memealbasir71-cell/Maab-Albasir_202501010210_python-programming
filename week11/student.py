def get_student():
    print("==== computer lab access ====")

    name = input("student name :")
    student_ID = input("student ID:")
    registered = input("register for today's lab?(Y/N):").upper()
    lab_open = input("is the lab open?(Y/N):").upper
    computer_available = input("compurte available?(Y/N):").upper()

    return name, student_ID, registered, lab_open, computer_available