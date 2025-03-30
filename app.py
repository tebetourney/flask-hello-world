from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Talia Betourney in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://talia_betourney_database_user:PiGIuxXpS96FG6tqbKT2KwLrdSeG0Hx4@dpg-cvkoc6be5dus73bsa8rg-a/talia_betourney_database")
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://talia_betourney_database_user:PiGIuxXpS96FG6tqbKT2KwLrdSeG0Hx4@dpg-cvkoc6be5dus73bsa8rg-a/talia_betourney_database")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'