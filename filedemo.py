faculty_file = open("requiredCS.txt", "r")
all_class_lines = faculty_file.readlines()
for class_line in all_class_lines:
    loud_line = class_line.upper()
    print(loud_line)
print("those are the courses you have to take")

