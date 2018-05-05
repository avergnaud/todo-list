from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from notes_manager import get_notes_from_calendar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

db.create_all()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/refresh')
def refresh():
    summariesSet = get_notes_from_calendar()
    for summary in summariesSet:
        todo = Todo(text=summary)
        db.session.add(todo)
        db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)