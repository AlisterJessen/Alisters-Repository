from flask import Flask, render_template

app = Flask(__name__)
DATABASE = "smile.db"

@app.route('/')
def render_homepage():
    return render_template('home.html')

def create_connection(db_file):
    try:
        connection = sqlite3.connection(db_file)
        return connection
    except Error as e:
        print(e)
    return none


@app.route('/hi')
def hi():
    return 'hello alister'


@app.route('/menu')
def render_menu_page():
    con = create_connection(DATABASE)

    query = "SELECT name, description, volume, price filename FROM product"
    cur = con.cursor() #Creates a cursor to wrist the query
    cur.execute(query) #runs the query
    product_list = cur.fetchall

    return render_template('menu.html', products=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
