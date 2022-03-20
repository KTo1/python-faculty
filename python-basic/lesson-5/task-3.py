
# Генератор дает эффект в тех случаях когда нужен выигрыш по памяти и не нужен доступ по случайному ключу
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '9В', '8Б', '10А'
]

for i in range(len(tutors) - len(klasses)):
    klasses.append(None)

classes_gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))

print(type(classes_gen))

print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))
print(next(classes_gen))

# This last
print(next(classes_gen))

# Raise StopIteration
# print(next(classes_gen))
