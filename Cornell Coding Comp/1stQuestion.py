t = input()
t = int(t)

students = []

for i in range(t):
    students.append(int(input()))

letters = []

for student in students:

    letters.append(student * (student - 1))

for i in letters:
    print(i)