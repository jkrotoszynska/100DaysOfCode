import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

studnets_score = {student:random.randint(1,100) for student in names}
print(studnets_score)

passed_students = {student:score for (student,score) in studnets_score.items() if score >= 60}
print(passed_students)