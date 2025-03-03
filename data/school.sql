DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS subjects;

CREATE TABLE teachers (
    id serial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    age integer,
    subject integer
);
CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    age integer, 
    subject integer
);
CREATE TABLE subjects (
    id serial PRIMARY KEY,
    subject varchar(255)
);

\copy teachers FROM 'data/teachers.csv' WITH (FORMAT csv, HEADER);
\copy students FROM 'data/student.csv' WITH (FORMAT csv, HEADER);
\copy subjects FROM 'data/subjects.csv' WITH (FORMAT csv, HEADER);
