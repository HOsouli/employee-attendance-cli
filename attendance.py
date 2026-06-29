import os
from datetime import datetime
import win32com.client as win32
from employee import check_staff


def speaker_device(attendance_type):
    """
    Play a voice message based on the attendance type.

    If the attendance type is 'in', it plays a welcome message.
    If the attendance type is 'out', it plays a goodbye message.

    Args:
        attendance_type (str): Either 'in' or 'out'.
    """
    speaker = win32.Dispatch('SAPI.SpVoice')
    speaker.Speak('welcome') if attendance_type == "in" else speaker.Speak("goodbye")

# _____________________________________________________________________________________
def get_attendance_type(staff_id, attendance):
    """
    Determine whether the next attendance record for a staff member
    should be 'in' or 'out' based on today's previous records.
    """
    today = datetime.now().strftime("%Y/%m/%d")
    last_row = None

    attendance.seek(0)
    data = attendance.readlines()

    for item in data[1:]:
        row = item.strip().split(",")

        if len(row) < 5:
            continue

        if row[1] == str(staff_id) and row[3] == today:
            last_row = row

    if last_row:
        if last_row[2] == "in":
            return "out"
        return "in"

    return "in"

# _____________________________________________________________________________________
def record_employee_attendance(staff_id):
    header = "ID,FK_ID,type,date,time"
    file_path = "database/staff_attendance.csv"
    os.makedirs("database", exist_ok=True)

    exists_file = os.path.exists(file_path)
    today = datetime.now().strftime("%Y/%m/%d")
    now_time = datetime.now().strftime("%H:%M:%S")
    number_id = 1

    with open(file_path, "a+", encoding="utf-8") as attendance:
        attendance.seek(0)

        if not exists_file:
            attendance.write(f"{header}\n")
            attendance.flush()

        attendance.seek(0)
        read_data = attendance.readlines()

        if len(read_data) > 1:
            number_id = int(read_data[-1].strip().split(",")[0]) + 1

        if check_staff(staff_id):
            attendance_type = get_attendance_type(staff_id, attendance)
            string_data = f"{number_id},{staff_id},{attendance_type},{today},{now_time}\n"
            attendance.write(string_data)
            attendance.flush()
            speaker_device(attendance_type)
        else:
            print("Cannot find any staff...")





