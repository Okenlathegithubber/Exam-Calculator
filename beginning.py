courses_cu = {
    "MTH-101" : "",
    "CSC-101" : "",
    "CHM-101" : "",
    "PHY-101" : "",
    "PHY-103" : "",
    "STA-105" : "",
    "GST-103" : "",
    "GST-105" : ""
}
total = 0
course_num = 0
for course in courses_cu.keys():
    score = int(input(f"Enter the score for {course} >> "))
    course_num += 1
    total += score
    average = total / course_num
    percentage = average * 100
print(total)
print(average)
print(percentage)