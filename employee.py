import os
from validate import validate_mobile

"""
row1= title
row2= data
"""
"title = emoloyee.csv: id, first_name, last_name, phone_number, post"

# ______________________________________________________________________
FILE_PATH = "database/staff_info.csv"

def save_employee_info():
    """
    Collect employee information from user input and store it in staff_info.csv.

    The function checks if the database directory and file exist. If the file
    does not exist, it creates it and writes the header. Then it generates a
    unique ID for each employee and appends the entered data to the CSV file.
    """
    header = "ID,first_name,last_name,phone_number,job"
    os.makedirs("database", exist_ok=True)
    file_exists = os.path.exists(FILE_PATH)
    number_id = 1
    with open(FILE_PATH, "+a", encoding="utf-8") as emp:
        emp.seek(0)

        if not file_exists:
            emp.write(f"{header}\n")
            emp.flush()
        else:
            read_data = emp.readlines()
            if len(read_data) > 1:
                number_id = int(read_data[-1].strip().split(",")[0]) + 1

        while True:
            data_staring = ""
            for title in header.strip().split(","):
                if title == "ID":
                    data_staring += f"{number_id},"
                elif title == "phone_number":
                    while True:
                        phone = input(f"Please enter data for {title}: ")

                        try:
                            validate_mobile(phone)
                            data_staring += f"{phone},"
                            break
                        except ValueError as e:
                            print(e)
                else:
                    data = input(f"Please enter data for {title}: ")
                    data_staring += f"{data},"
                    if data_staring == "phone_number":
                        data_staring.validate_mobile()
            emp.write(f"{data_staring[:-1]}\n")
            emp.flush()

            number_id += 1

            ans = input("Do you want to countinue? Y/N: ")
            if ans.lower() == "n":
                break

    print("Data registered successfully.")

# save_employee_info()

# ___________________________________________________________________________
def check_staff(staff_id):
    """
    Check whether a given staff ID exists in the staff_info.csv file.

    Args:
        staff_id (str | int): The employee ID to search for.

    Returns:
        bool: True if the staff ID exists, otherwise False.
    """
    if not os.path.exists(FILE_PATH):
        return False
    with open("database/staff_info.csv", "r") as emp:
        data = emp.readlines()
        for item in data[1:]:
            row = item.strip().split(",")
            if row[0] == str(staff_id):
                return True

        return False


