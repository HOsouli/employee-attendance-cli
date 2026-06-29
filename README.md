# Employee Attendance Management System

A simple employee attendance management system built with Python.

This project allows registering employees, storing employee information in CSV files and recording attendance (Clock In / Clock Out) with automatic attendance status detection.

---

## Features

- 👤 Register new employees
- 💾 Store employee data in CSV
- 📱 Validate mobile number format
- ⏱️ Record attendance (Clock In / Clock Out)
- 🔁 Automatic attendance type detection
- 🔊 Voice notification (Welcome / Goodbye)
- 🧩 Modular project structure

---

## Project Structure

```text
project/
│
├── main.py
├── employee.py
├── attendance.py
├── validate.py
│
├── database/
│   ├── staff_info.csv
│   └── staff_attendance.csv
│
└── README.md
```

---

## Requirements

Install dependencies:

```bash
pip install pywin32
```

---

## Run Project

```bash
python main.py
```

---

## Example Workflow

### Register Employee

```text
Please enter data for first_name:
Please enter data for last_name:
Please enter data for phone_number:
Please enter data for job:
```

### Record Attendance

```text
Enter your staff ID:
→ Welcome
→ Goodbye
```

---

## Future Improvements

- Django version
- PostgreSQL
- REST API
- Authentication
- Dashboard
- Attendance Reports
- Device Integration

---

## Technologies Used

- Python
- CSV
- Regex
- File Handling
- win32com.client

---

## Author

Hossein Osooli

---

⭐ CLI version — foundation for future Django + PostgreSQL attendance system.
:::
