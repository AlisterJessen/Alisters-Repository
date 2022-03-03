from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "smile.db"



@app.route('/')
def render_homepage():
    return render_template('home.html')

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/hi')
def hi():
    return 'hello alister'


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)

    query = "SELECT name, description, volume, price, image FROM product"
    cur = con.cursor() #Creates a cursor to wrist the query
    cur.execute(query) #runs the query
    product_list = cur.fetchall()

    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')

@app.route('/signup')
def render_signup_page():
    return render_template('signup.html')

@app.route('/login')
def render_login_page():
    return render_template('login.html')





app.run(host='0.0.0.0', debug=True)
