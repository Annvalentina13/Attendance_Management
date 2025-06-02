# 📋 Attendance Management System (Tkinter + CSV)

This project is a beginner-friendly **Attendance Management System** developed using **Python** and **Tkinter**, Python’s standard GUI toolkit. It allows users to mark attendance, add new students, and export attendance data to a CSV file. The system is ideal for small-scale usage like classroom attendance, club activities, or training programs.

---

## 🧾 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [CSV Output Example](#csv-output-example)
- [Future Improvements](#future-improvements)


---

## ✅ Features

- 👤 **Predefined Student List** – Includes default students (John, Mary, Sam, Alice, Bob)
- ➕ **Add New Students Dynamically** – Extend your list instantly through GUI
- ✅ **Mark Present/Absent** – Use dropdowns to mark attendance for each student
- 💾 **Export to CSV File** – Save attendance logs with timestamped filenames
- 🔁 **Clear Attendance Data** – Reset the form without closing the app
- 🚪 **Exit Button** – Clean and fast exit
- 🖼️ **Responsive & Styled GUI** – Clean layout with color-coded sections and labels

---

## 🛠️ Technologies Used

| Technology | Purpose             |
|------------|---------------------|
| Python     | Core logic          |
| Tkinter    | Graphical Interface |
| CSV module | File export         |
| Datetime   | Auto timestamping   |

No external libraries or installations are required. All used libraries are included in the Python Standard Library.

---

## 🔍 How It Works

1. 🖥 **Startup**:
   - Loads a predefined student list.
   - Displays each student with a dropdown menu to mark "Present" or "Absent".

2. ➕ **Adding Students**:
   - Enter a student name in the input field and click "Add Student".
   - The new name will appear in the list.

3. ✅ **Submitting Attendance**:
   - All students must have a status selected.
   - Click "Submit Attendance" to store data in memory.

4. 💾 **Exporting Attendance**:
   - Click "Export to CSV".
   - A file named like `Attendance_2025-06-02_14-23.csv` will be created in the same directory.

5. 🔄 **Clear**:
   - Resets all status selections to "None".

6. 🚪 **Exit**:
   - Closes the application window.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

---

## 🗃 Project Structure

attendance-tkinter/
- ├── attendance_system.py     # Main application file
- ├── README.md                # This documentation
- └── *.csv                    # Attendance logs (auto-generated)

---

## 📁 CSV Output Example

A file named Attendance_2025-06-02_14-23.csv may look like this:

- Student Name,Status,Date
- John,Present,2025-06-02
- Mary,Absent,2025-06-02
- Sam,Present,2025-06-02
- Alice,Present,2025-06-02
- Bob,Absent,2025-06-02

--- 

## 💡 Future Improvements

- Store attendance permanently (SQLite or Pandas DataFrame)
- Add calendar/date selection
- View attendance history
- Face recognition integration (OpenCV)


