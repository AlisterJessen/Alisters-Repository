from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "app.secret_key"
DATABASE = "smile.db"



def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def render_homepage():
    return render_template('home.html')



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



@app.route('/logout')
def render_logout_page():
    [session.pop(key) for key in list(session.keys())]
    print(list(session.keys()))
    return redirect('/?message=see+you+next+time')

def is_logged_in():
    if session.get('email') is None:
        print("not logged in")
        return False
    else:
        print("Logged in")
        return True



@app.route('/signup', methods=['GET', 'POST'])
def render_signup_page():
   if request.method == 'POST':
    print(request.form)
    fname = request.form.get('fname').title().strip()
    lname = request.form.get('lname').title().strip()
    email = request.form.get('email').title().strip()
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if not password != password2:
        return redirect('/signup.html?error=Passwords+do+not+match')

    if len(password) < 8:
        return redirect('/signup.html?error=Passwords+must+be+at+least+8+characters')

    hashed_password = bcrypt.genarate_passwrod_hash(password)

    con = create_connection(DATABASE)

    query = "INSERT INTO customer (fname, lname, email, password) VALUES(?,?,?,?)"

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def render_login_page():
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email').lower().strip()
        password = request.form.get('password')
        hashed_password = request.form.get('password')

        con = create_connection(DATABASE)
        query = "SELECT id, fname FROM customer WHERE email=? AND password=?"
        cur = con.cursor()
        cur.execute(query, (email, password))
        user_data = cur.fetchall()
        con.close()

        if user_data:
            user_id = user_data[0][0]
            first_name = user_data[0][1]
            db_password = user_data[0][2]
        else:
            return redirect("/login?error=Email+or+password+is+incorrect")
        print(user_id, first_name)
        if not bcrypt.check_password_hash(db_password, password):
            return redirect("/login?error=Email+or+password+is+incorrect")

        session['email'] = email
        session['userid'] = user_id
        session['fname'] = first_name
        session['cart'] = []
        return redirect('/menu')




    return render_template('login.html')

app.run(host='0.0.0.0', debug=True)













