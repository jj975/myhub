import calendar

while True:
    choice = input("Hello there!!! \nEnter '1' to display the calendar for the current month, or '2' to display the calendar for another month, or 'q' to quit: ")

    if choice == 'q':
        break

    elif choice == '1':
        year = calendar.datetime.datetime.now().year
        month = calendar.datetime.datetime.now().month
        print(calendar.month(year, month))

    elif choice == '2':
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        print(calendar.month(year, month))

    else:
        print("Invalid choice.")
