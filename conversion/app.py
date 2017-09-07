from flask import Flask, render_template
import sqlite3



app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/print_items')
def print_items():
    db = sqlite3.connect('/home/ricardo/projects/ireland/app/data/leads.db')
    cursor = db.cursor()
    cursor.execute('SELECT name, link FROM linkedinleads')
    return render_template('print_items.html', items=cursor.fetchall())

if __name__ == "__main__":
    app.run(debug = True)
