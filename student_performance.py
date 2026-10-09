import pandas as pd

names = [
    "Aarav", "Diya", "Kabir", "Meera", "Rohan", "Anaya", "Arjun", "Isha",
    "Vivaan", "Sana", "Aditya", "Kiara", "Reyansh", "Myra", "Ishaan",
    "Pari", "Dev", "Aanya", "Krish", "Tara", "Ayaan", "Nisha", "Rahul",
    "Priya", "Karan", "Simran", "Neel", "Riya", "Varun", "Pooja",
    "Mohan", "Kavya", "Yash", "Zara", "Manav", "Ira", "Dhruv", "Sara",
    "Om", "Tanya", "Rudra", "Aditi", "Jay", "Navya", "Veer", "Mira",
    "Sahil", "Anika", "Arnav", "Sia", "Harsh", "Reva", "Ritvik", "Naina",
    "Akhil", "Lavanya", "Kunal", "Esha", "Sameer", "Tia"
]

# Each record contains:
# name, roll number, attendance %, assignments submitted (out of 10),
# lab performance (out of 100), CGPA (out of 10), total marks (out of 500)
records = []

for i, name in enumerate(names):
    attendance = 55 + ((i * 13 + 7) % 46)
    assignments = 4 + ((i * 3 + 2) % 7)
    lab_performance = 50 + ((i * 17 + 11) % 51)
    total_marks = 250 + ((i * 37 + 23) % 251)
    cgpa = round(total_marks / 50, 1)

    records.append({
        "name": name,
        "roll_no": 101 + i,
        "attendance": attendance,
        "assignments_submitted": assignments,
        "lab_performance": lab_performance,
        "cgpa": cgpa,
        "total_marks": total_marks
    })

df = pd.DataFrame(records)

# Assign a performance category based on total marks
def get_performance(marks):
    if marks >= 400:
        return "High"
    elif marks >= 325:
        return "Average"
    else:
        return "Low"

df["performance"] = df["total_marks"].apply(get_performance)

search = input("Enter student name or roll number: ").strip()

if search.isdigit():
    matches = df[df["roll_no"].astype(str) == search]
else:
    matches = df[df["name"].str.casefold() == search.casefold()]

if matches.empty:
    print("Student not found. Check the name or roll number.")
else:
    student = matches.iloc[0]

    print("\n========== STUDENT PERFORMANCE ==========")
    print("Name:", student["name"])
    print("Roll Number:", student["roll_no"])
    print("Attendance:", str(student["attendance"]) + "%")
    print("Assignments Submitted:",
          str(student["assignments_submitted"]) + "/10")
    print("Lab Performance:", str(student["lab_performance"]) + "/100")
    print("CGPA:", str(student["cgpa"]) + "/10")
    print("Total Marks:", str(student["total_marks"]) + "/500")
    print("Overall Performance:", student["performance"])

    if student["performance"] == "Low":
        print("Suggestion: Consider additional academic support.")
    elif student["performance"] == "Average":
        print("Suggestion: Keep practicing and completing assignments.")
    else:
        print("Suggestion: Keep up the good work!")

    print("==========================================")
