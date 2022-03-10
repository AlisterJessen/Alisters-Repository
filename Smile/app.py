from flask import Flask, render_template, request, redirect
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



p.route('/signup', methods=['GET', 'POST'])
def render_signup_page():
   if request.method == 'POST':
    print(request.form)
    frame = request.form.get('fname').title().strip()
    lname = request.form.get('lname').title().strip()
    email = request.form.get('email').title().strip()
    password = request.form.get('password')
    pasword2 = request.form.get('password2')

    if passwrod != password2:
        return redirect('/signup.html?error=Passwrods+do+not+match')

    if len(password) < 8:
        return redirect('/signup.html?error=Passwrods+must+be+at+least+8+characters')

    con = create_connection(DATABASE)


    query = "INSERT INTO customer (fname, lname, email, password) VALUES(?,?,?,?)"

    return render_template('signup.html')

@app.route('/login')
def render_login_page():

def render_signup_page():
   if request.method == 'POST':
    print(request.form)
    email = request.form.get('email').title().strip()
    password = request.form.get('password')

    con = create_connection(DATABASE)
    query = "SELECT fname FROM product WHERE email=? AND password=?"\
    cur = con.cursor()
    cur.execute(query, (email, password))
    user.data = cur.fetchall()
    con.close()

    try:
        user_id = user_data[0][0]
        first_name = user_data[0][1]
    except indexError:
        return redirect("login?error=Email+or+password+is+incorrect")
    print(user_id, first_name)

    return render_template('login.html')

app.run(host='0.0.0.0', debug=True)













