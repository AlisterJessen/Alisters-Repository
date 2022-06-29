from flask import Flask, render_template, request, redirect, session
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
# bcrypt = Bcrypt(app)
app.secret_key = "ffw5eg43r"
DATABASE = "C:/Users/21438/OneDrive - Wellington College/y13/dts 2022/Maori Dictionary/Maori Dictionary/Maori Dictionary/Dictionary.db"


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

def get_categories():
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute("select distinct category from category")
    results = cur.fetchall()
    con.close()
    return results

@app.route('/')
def render_homepage():
    return render_template('home.html', categories=get_categories())


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)

    query = "SELECT maori, english, category, definition FROM category"

    cur = con.cursor()  # Creates a cursor to wrist the query
    cur.execute(query)  # runs the query
    category_list = cur.fetchall()
    con.close()

    return render_template('2menu.html', categories=category_list)




@app.route('/signup', methods=['GET', 'POST'])
def render_signup_page():
   if request.method == 'POST':
       print(request.form)
       fname = request.form.get('fname')
       lname = request.form.get('lname')
       email = request.form.get('email')
       password = request.form.get('password')
       password2 = request.form.get('password2')



       hashed_password = bcrypt.genarate_passwrod_hash(password)

       con = create_connection(DATABASE)

       query = "INSERT INTO customer (id, fname, lname, email, password) VALUES(NULL,?,?,?,?)"

       cur = con.cursor()  # Creates a cursor to wrist the query
       cur.execute(query, (fname, lname, email, password))  # runs the query
       con.commit()
       con.close()

   return render_template('signup.html')





@app.route('/login', methods=['GET', 'POST'])
def render_login_page():
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email').lower().strip()
        password = request.form.get('password').strip()
        hashed_password = request.form.get('password')


        query = "SELECT id, fname FROM customer WHERE email AND password"
        con = create_connection(DATABASE)
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
        return redirect('/menu')




    return render_template('login.html')















app.run(host='0.0.0.0', debug=True)
