from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('students.db')
    conn.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)')
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        conn = sqlite3.connect('students.db')
        conn.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
        conn.commit()
        conn.close()
        return redirect('/view')
    return render_template('add_student.html')

@app.route('/view')
def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('view_students.html', students=students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
