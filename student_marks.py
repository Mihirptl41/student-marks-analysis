
# Student Marks Analysis
# Author: Mihir Patel

students = {
    "Amit": 85,
    "Rahul": 72,
    "Priya": 95,
    "Neha": 88,
    "Karan": 65
}

print("===== STUDENT MARKS ANALYSIS =====")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("\nAverage Marks:", average)
print("Highest Scorer:", highest, "-", students[highest])
print("Lowest Scorer:", lowest, "-", students[lowest])
