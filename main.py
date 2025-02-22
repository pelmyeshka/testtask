import random
students = ['Арсений', 'Паша', 'Александра', 'Олег', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Добавить нового ученика
5. Удалить ученика из списка
6. Добавить новый предмет
7. Удалить школьный предмет
8. Изменить оценку ученика
9. Вывод оценок для определенного ученика
10. Вывод среднего балла по каждому предмету по определенному ученику
11. Выход из программы
''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                if students_marks[student][class_]:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Добавить нового ученика')
        name = input('Введите имя ученика которого нужно добавить: ')
        if name in students:
            print('Такой ученик уже есть в списке')
        else:
            students.append(name)
            students_marks[name] = {}
            for class_ in classes:
                students_marks[name][class_] = []
            print('Ученик успешно добавлен')
            print(students)
    elif command == 5:
        print('5. Удалить ученика из списка')
        name = input('Введите имя ученика которого нужно удалить из списка: ')
        if name in students:
            students.remove(name)
            print('Успешно удален из списка')
            print(students)
        else:
            print('Такого ученика нет в списке')
    elif command == 6:
        print('6. Добавить новый предмет')
        subject = input('Введите название предмета, который нужно добавить: ')
        if subject in classes:
            print('Предмет уже есть в списке')
        else:
            classes.append(subject)
            for student in students_marks:
                students_marks[student][subject] = []
            print('Предмет успешно добавлен в список')
            print(classes)
    elif command == 7:
        print('7. Удалить школьный предмет')
        subject = input('Введите название предмета, который нужно удалить: ')
        if subject in classes:
            classes.remove(subject)
            print('Предмет успешно удален из списка')
            print(classes)
        else:
            print('Такого предмета нет в списке')
    elif command == 8:
        print('8. Изменить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            print(students_marks[student][class_])
            num_0 = int(input('Введите индекс оценки которую хотите изменить: '))
            num_1 = int(input('Введите новую оценку: '))
            students_marks[student][class_][num_0] = num_1
            print('Оценка изменена')
    elif command == 9:
        print('9. Вывод оценок для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f'Оценки ученика {student}:')
            for subject, marks in students_marks[student].items():
                print(f'{subject}: {marks}')
        else:
            print('Ученик не найден')
    elif command == 10:
        print('10. Вывод среднего балла по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students and student in students_marks:
            print(f'Средний балл {student}:')
            for class_ in classes:
                if students_marks[student][class_]:
                    marks_sum = sum(students_marks[student][class_])
                    marks_count = len(students_marks[student][class_])
                    print(f'{class_} - {marks_sum // marks_count}')
        else:
            print('Ученик не найден')

    elif command == 11 :
            print('11. Выход из программы')
            break
