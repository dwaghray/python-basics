# replicates the listing of undergraduate Informatics courses at IU from a file
# using a dictionary to store and print course codes and names

with open("INFOcourses.txt", "r") as f:
    course_data = f.readlines()

courses = {}
for line in course_data:
    code, name = line.split(", ")
    courses[code] = name.strip()

print("Information on", len(courses.keys()), "courses loaded.")

while True:
    lookup = input("Enter a course code or STOP: ")

    if lookup.upper() == "STOP":
        break

    print("The name of that course is", courses.get(lookup, "not found"), ".")
