from ticket import create_ticket
from display import display_ticket

def main():
    name, student_ID, issue, location, priority = create_ticket()
    if priority.lower() == "High":
        technicion = "Ahmad"
    elif priority.lower() == "Medium":
        technicion = "Siti"
    else:
        technicion = "Ali"
    status = "Pending"

    display_ticket(
        name,
        student_ID,
        issue,
        location,
        priority,
        technicion,
        status
    )
if __name__ == "__main__":
    main()