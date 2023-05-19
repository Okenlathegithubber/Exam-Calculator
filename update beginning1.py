total_credit_unit = 28
courses_cu = {
    "MTH-101" : 3.5,
    "CSC-101" : 3.5,
    "CHM-101" : 3.5,
    "PHY-101" : 3.5,
    "PHY-103" : 3.5,
    "STA-105" : 3.5,
    "GST-103" : 3.5,
    "GST-105" : 3.5
}

letter_grade_range = {
    "A": 4.00,
    "AB": 3.50,
    "B": 3.25,
    "BC": 3.00,
    "C": 2.75,
    "CD": 2.50,
    "D": 2.25,
    "E": 2.00,
    "F": 0.00
}

for course in courses_cu.keys():
    score = int(input(f"Enter the score of {course} >> "))

def letter_grade_to_score(score):
    if score >= 75:
        return "A"
    elif score >= 70:
        return "AB"
    elif score >= 65:
        return "B"
    elif score >= 60:
        return "BC"
    elif score >= 55:
        return "C"
    elif score >= 50:
        return "CD"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


for course in courses_cu.keys():
    letter_grade = letter_grade_to_score(score)
    print(f"{course}: {score} ({letter_grade})")