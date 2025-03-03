all_teachers = [
    {'id': 1, 'first_name': 'Chase', 'last_name': 'Coleman', 'age': 26, 'subject': 'Science'},
    {'id': 2, 'first_name': 'Brian', 'last_name': 'Kim', 'age': 26, 'subject': 'Math'},
    {'id': 3, 'first_name': 'Ian', 'last_name': 'Tank', 'age': 25, 'subject': 'Engineering'},
    {'id': 4, 'first_name': 'Anne', 'last_name': 'Chhing', 'age': 26, 'subject': 'Science'},
]
all_students = [
    {'id': 1,'first_name': 'Jim','last_name': 'Halpert','age': 27,'subject': 'Math'},
    {'id': 2,'first_name': 'Pam','last_name': 'Beesly','age': 25,'subject': 'Science'},
    {'id': 3,'first_name': 'Dwight','last_name': 'Schrute','age': 31,'subject': 'Engineering'},
    {'id': 5,'first_name': 'Michael','last_name': 'Scott','age': 38,'subject': 'Science'},
]
all_subjects = [
    {'id': 4, 'subject_name': 'Math'},
    {'id': 4, 'subject_name': 'Science'},
    {'id': 4, 'subject_name':' History'}
]

def get_teachers():
    teachers = [{'id': teacher['id'], 'first_name': teacher['first_name'], 'last_name': teacher['last_name'], 'age': teacher['age'], 'subject': teacher['subject']} for teacher in all_teachers]
    # teachers.append({'id': teacher['id'], 'first_name': teacher['first_name'], 'last_name': teacher['last_name'], 'age': teacher['age'], 'subject': teacher['subject']} for teacher in all_teachers)
    print(*teachers)
def get_students():
    students = [{'id': teacher['id'], 'first_name': teacher['first_name'], 'last_name': teacher['last_name'], 'age': teacher['age'], 'subject': teacher['subject']} for teacher in all_teachers]
    # teachers.append({'id': teacher['id'], 'first_name': teacher['first_name'], 'last_name': teacher['last_name'], 'age': teacher['age'], 'subject': teacher['subject']} for teacher in all_teachers)
    # print(*students)
    return students
def get_subjects():
    subjects = [{'id': teacher['id'], 'first_name': teacher['first_name'], 'last_name': teacher['last_name'], 'age': teacher['age'], 'subject': teacher['subject']} for teacher in all_teachers]
    for sub in subjects:
        for stu in get_students():
            print stu.subject
    print(*subjects)



get_teachers()
get_students()
get_subjects()