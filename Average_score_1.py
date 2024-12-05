grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

alfavit_students = list(sorted(students))
gr_A = sum(grades[0]) / len(grades[0])
gr_B = sum(grades[1]) / len(grades[1])
gr_J = sum(grades[2]) / len(grades[2])
gr_K = sum(grades[3]) / len(grades[3])
gr_S = sum(grades[4]) / len(grades[4])
average_score_students = dict([['Johnny', gr_A], ['Bilbo', gr_B], ['Johnny', gr_J], ['Khendrik', gr_K], ['Steve', gr_S]])
print(average_score_students)