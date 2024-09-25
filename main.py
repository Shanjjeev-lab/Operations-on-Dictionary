students = {"name": "Ash", "roll": 1, "age": 10, "subject": "Science, Math, Geography"}

print(students)

print("Students name: ", students["name"])
print("Students roll: ", students["roll"])
print("Students age: ", students.get("age"))

students["age"] = 10
print(students)

students["address"] = "1234 Beckingham Street, London, England"
print(students)

students.clear()
print("Clearing the dictionary:", students)