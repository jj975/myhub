import calendar

while True:
    # Ask the user which month to display the calendar for
    choice = input("Hello there!!! \nEnter '1' to display the calendar for the current month, or '2' to display the calendar for another month, or 'q' to quit: ")

    # If the user chooses to quit
    if choice == 'q':
        break

    # If the user chooses the current month
    elif choice == '1':
        year = calendar.datetime.datetime.now().year
        month = calendar.datetime.datetime.now().month
        print(calendar.month(year, month))

    # If the user chooses another month
    elif choice == '2':
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        print(calendar.month(year, month))

    # If the user enters an invalid choice
    else:
        print("Invalid choice.")
