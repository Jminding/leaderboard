from flask import *
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('database.db', check_same_thread=False)
db = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        score = request.form['score']
        db.execute("INSERT INTO LEADERBOARD VALUES (?, ?)", (name, score))
        conn.commit()
    data = dict(sorted(dict(db.execute("SELECT * FROM LEADERBOARD")).items(), key=lambda x: int(x[1]), reverse=True))
    return render_template('index.html', data=data)

@app.route('/user/<username>')
def profile(username):
    data = dict(sorted(dict(db.execute("SELECT * FROM LEADERBOARD")).items(), key=lambda x: int(x[1]), reverse=True))
    return render_template('profile.html', name=username, score=data[username])