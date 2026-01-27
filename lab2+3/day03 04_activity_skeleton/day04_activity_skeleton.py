"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""

students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}

# TODO: Implement the tasks above using nested dict access.
#the accessing nested
print(students["S001"]["courses"]["AI301"]["grade"])
#try the safe way
print(students.get("S001", {}).get("courses", {}).get("AI301", {}).get("grade", 0))

total_points = 0
total_credits = 0
for course in students["S002"]["courses"].values():
    total_points+=course["grade"]*course["credits"]
    total_credits+=course["credits"]

bob_gpa=total_points/total_credits
print(bob_gpa)

cs101_students=[]
for sid, info in students.items():
    if "CS101" in info["courses"]:
        cs101_students.append(info["name"])

print(cs101_students)

grades=[]

for info in students.values():
    for course in info["courses"].values():
        grades.append(course["grade"])

average_grade=sum(grades)/len(grades)
print(average_grade)


def calc_gpa(student):
    total_points = 0
    total_credits = 0
    for course in student["courses"].values():
        total_points += course["grade"] * course["credits"]
        total_credits += course["credits"]
    return total_points / total_credits

best_student = None
best_gpa = 0

for info in students.values():
    gpa = calc_gpa(info)
    if gpa > best_gpa:
        best_gpa = gpa
        best_student = info["name"]

print(best_student, best_gpa)
