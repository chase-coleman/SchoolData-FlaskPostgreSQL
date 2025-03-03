from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask("app")
app.config['SQLALCHEMY-DATABASE_URI'] = (
    'postgresql://chasecoleman@localhost/school'
)
db = SQLAlchemy(app)


class Teachers(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Subjects(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))


# getting the teachers
@app.route('/teachers/', methods=["GET"])
def get_teachers():
    all_teachers = Teachers.query.all()
    print(all_teachers)