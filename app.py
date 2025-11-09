from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)
models.init_db()

@app.route('/')
def index():
    students = models.query("SELECT * FROM students")
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        models.query("INSERT INTO students (student_id,name,grade,course) VALUES (?,?,?,?)",
                    (request.form['student_id'], request.form['name'], 
                     request.form['grade'], request.form['course']))
        return redirect(url_for('index'))
    return render_template('add_edit.html', student=None)

@app.route('/delete/<id>')
def delete(id):
    models.query("DELETE FROM students WHERE id=?", (id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
