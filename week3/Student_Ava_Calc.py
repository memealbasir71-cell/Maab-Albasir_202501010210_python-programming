choice = "Y"

# Start the program and repeat while the user chooses Y

while choice == "Y":


    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))


    average = (quiz_1 + quiz_2 + quiz_3) / 3


    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    print("Average:", average)

    choice = input("Continue? Select Y/N: ").upper()

print("Program Ended")