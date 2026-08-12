## Lab Computer Monitoring System
A simple Python console program that lets a lab attendant record and monitor the status of 5 lab computers in repeating cycles.

## Files Purposes
main.py: Runs the main monitoring loop
check_computers.py:
Prompts user for each computer's status 
count_available.py: Counts how many computers are marked "Available" 
display_status.py: Prints a formatted lab status report

## How It Works
check_computers() — Loops through Computers 1–5, asking the user to enter a status for each: A = Available U = Used M = Maintenance Returns a list of the 5 statuses. count_available(computers) — Counts and returns how many entries in the list equal "A". display_status(computers, available) — Prints a formatted report showing each computer's number and status, plus the total available count. Main loop — Repeats the above steps, then asks the user if they want to run another cycle (Y/N). Entering N ends the program.