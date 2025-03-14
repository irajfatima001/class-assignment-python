
    
# 🎓📜 Student Report Card Management System

students = []  # 📂 List to store all student records

def calculate_grade(percentage):
    """🏆 Assign Grade Based on Percentage"""
    if percentage >= 80:
        return "🌟 A+ (Excellent)"
    elif percentage >= 70:
        return "🎯 A (Very Good)"
    elif percentage >= 60:
        return "📚 B (Good)"
    elif percentage >= 50:
        return "✅ C (Satisfactory)"
    elif percentage >= 40:
        return "⚠️ F (Needs Improvement)"
    else:
        return "❌ Fail (Try Again)"

while True:
    print("\n📝 Enter Student Details:")
    name = input("👩‍🎓 Enter Student Name: ")
    roll_no = input("🆔 Enter Roll Number: ")

    subjects = ["📐 Math", "🧪 Physics", "📖 Urdu", "📜 English", "💻 Computer"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                marks[subject] = float(input(f"✏️ Enter marks for {subject}: "))
                if marks[subject] < 0 or marks[subject] > 100:
                    print("❌ Marks must be between 0 and 100. Try again!")
                    continue
                break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    # 📊 Calculate total marks & percentage
    total_marks = sum(marks.values())
    percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100
    grade = calculate_grade(percentage)

    # 📌 Store student data
    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade
    })

    print(f"\n✅ Record of {name} inserted successfully. 🎉")

    # ❓ Ask user if they want to continue
    choice = input("\n🔄 Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().lower()
    if choice != "y":
        break  # 🛑 Exit the loop

# 📌 Show all students' records
print("\n🎓📊 All Students Report Cards:")
for student in students:
    print("\n" + "=" * 10)
    print(f"📌 Name: {student['name']}")
    print(f"🆔 Roll Number: {student['roll_no']}")
    print("*-----------📜-----------*")
    for subject, mark in student["marks"].items():
        print(f"📌 {subject}: {mark} ")
    print("*-----------📜-----------*")
    print(f"📊 Total Marks: {student['total_marks']} / 500")
    print(f"📈 Percentage: {student['percentage']:.2f}%")
    print(f"🏆 Grade: {student['grade']}")
    print("=" * 10)



