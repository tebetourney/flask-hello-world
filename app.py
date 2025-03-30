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
