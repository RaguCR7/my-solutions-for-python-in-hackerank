n = int(input('give us an input for the value:'))
student_marks = {}
for i in range(n):
    name, *line = input('give us an input for name:').split()
    score = list(map(float, line))
    student_marks[name] = score
query_name = input('Give us a query name:')

if query_name in student_marks:
    x = ((float(student_marks[query_name][0]) +
          float(student_marks[query_name][1]) + float(student_marks[query_name][2])) / 3)

print('%.2f' % 3)
