from employee import save_employee_info
from attendance import record_employee_attendance


def main():
    while True:
        print("\n--- Attendance & Employee Management System ---")
        print("1. Register New Employee")
        print("2. Record Attendance (Clock In/Out)")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            save_employee_info()
        elif choice == "2":
            staff_id = input("Enter your staff ID to clock in/out: ")
            record_employee_attendance(staff_id)
        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
