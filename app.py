import sqlite3 as sql
from flask import Flask, render_template, redirect, request, url_for
import database.database_interactions as db_interaction
#import custom modules for database


dbCon = sql.connect("database/invoice_genie.db", check_same_thread=False)
dbCursor = dbCon.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_client', methods=["POST", "GET"])
def add_client():
    fname = request.form['client_fname'].title()
    lname = request.form['client_lname'].title()
    rate = request.form['client_rate'].title()
    hours = request.form['client_hours'].title()
    paid = request.form['client_payment'].title()

    db_interaction.insert(dbCon, dbCursor, fname,lname,rate,hours,paid)


    data = db_interaction.read_table(dbCursor, 'clients')
    return render_template('table.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
