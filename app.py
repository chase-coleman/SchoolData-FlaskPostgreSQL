from flask import Flask, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict

app = Flask("app")
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://chasecoleman:password@localhost:5432/school'
)
db = SQLAlchemy(app)

class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

class Subjects(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

# Helper function
def get_all_data():
    all_students = Students.query.all()
    all_teachers = Teachers.query.all()
    all_subjects = Subjects.query.all()
    teachers = [{'id': teacher.id, 
                'first_name': teacher.first_name, 
                'last_name': teacher.last_name, 
                'age': teacher.age, 
                'subject': teacher.subject
                } for teacher in all_teachers
                ]
    students = [{'id': student.id, 
                'first_name': student.first_name, 
                'last_name': student.last_name, 
                'age': student.age, 
                'class': student.subject
                } for student in all_students
                ]
    subjects = [{'id': subject.id, 
                'subject_name': subject.subject
                } for subject in all_subjects
                ]
    return teachers, students, subjects

# getting the teachers
@app.route('/teachers', methods=["GET"])
def get_teachers():
    teachers, students, subjects = get_all_data()
    # loops thru every teacher and sets the subject key's value to a dict of subject name and students in class
    for teach in teachers:
        teacher_subject = teach['subject']
        students_in_class = []
        for stu in students:
            if stu['class'] == teacher_subject:
                stu_name = f"{stu['first_name']} {stu['first_name']}"
                students_in_class.append(stu_name)
        for sub in subjects:
            if sub['id'] == teacher_subject:
                teachers_subject = sub['subject_name']
        teach['subject'] = {'subject': teachers_subject, 'students': students_in_class}
    
    return jsonify(teachers)

@app.route('/students', methods=["GET"])
def get_students():
    teachers, students, subjects = get_all_data()
    # sets the students class value as their subject and teacher
    for student in students:
        stu_class = student['class']                    # sets the current iterations variable 
        for subject in subjects:                        # loops thru subject list
            if subject['id'] == stu_class:              # checks if classes id == students class id  
                class_name = subject['subject_name']    # sets class name as matching subject
        for teacher in teachers:                        # loops through teachers list
            if teacher['subject'] == stu_class:         # checks if teachers subject matches students class id
                teacher_name = f"{teacher['first_name']} {teacher['last_name']}"    # sets teacher name
        student['class'] = {'subject': class_name, 'teacher': teacher_name}     # creates dictionary to append to each students class value
    return jsonify(students)

@app.route('/subjects', methods=["GET"])
def get_subjects():
    teachers, students, subjects = get_all_data()
    # create a dictionary for each subject
    math = {'subject': 'Math'}
    science = {'subject': 'Science'}
    english = {'subject': 'English'}
    history = {'subject': 'History'}
    pe = {'subject': 'PE'}
    for teacher in teachers:
        t_sub = teacher['subject']
        t_name = teacher['first_name'] + ' ' + teacher['last_name']
        if t_sub == 1:
            math['teacher'] = t_name
        elif t_sub == 2:
            science['teacher'] = t_name
        elif t_sub == 3:
            english['teacher'] = t_name
        elif t_sub == 4:
            history['teacher'] = t_name
        else:
            pe['teacher'] = t_name
    math['students'] = list(filter(lambda stu : stu['class'] == 1, students))
    science['students'] = list(filter(lambda stu : stu['class'] == 2, students))
    english['students'] = list(filter(lambda stu : stu['class'] == 3, students))
    history['students'] = list(filter(lambda stu : stu['class'] == 4, students))
    pe['students'] = list(filter(lambda stu : stu['class'] == 5, students))
    return jsonify([math, science, english, history, pe])
    # loop through both teachers/students list & see if their subject value matches the current subject id

@app.route('/', methods=["GET"])
def home():
    return "<h1>Hello</h1>"
app.run(debug=True, port=8000)