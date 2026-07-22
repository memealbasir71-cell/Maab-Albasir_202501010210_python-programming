def create_ticket():
    name = input("Enter name: ")
    student_ID = input("Enter student ID: ")
    issue = input("Enter the issue you are facing: ")
    location = input("Enter location: ")
    priority = input("Enter the priority (High, Medium, Low): ")

    return (
         name, 
         student_ID, 
         issue, 
         location, 
         priority
    )