print("🔥 THIS IS MY NEW APP.PY 🔥")


from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS flights(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        source TEXT,
        destination TEXT,
        departure TEXT,
        arrival TEXT,
        price INTEGER,
        date TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS bookings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        passenger TEXT,
        flight TEXT,
        route TEXT,
        price INTEGER)''')

    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        user = c.fetchone()
        conn.close()

        if user:
            session['user'] = u
            return redirect('/dashboard')
        else:
            return "Invalid Login"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO users(username,password) VALUES(?,?)",(u,p))
        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/add_flight', methods=['GET','POST'])
def add_flight():
    if request.method == 'POST':
        data = (
            request.form['name'],
            request.form['source'],
            request.form['destination'],
            request.form['departure'],
            request.form['arrival'],
            request.form['price'],
            request.form['date']
        )

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO flights(name,source,destination,departure,arrival,price,date) VALUES(?,?,?,?,?,?,?)", data)
        conn.commit()
        conn.close()

        return "Flight Added Successfully"

    return render_template('add_flight.html')

@app.route('/search', methods=['GET','POST'])
def search():
    flights = []
    if request.method == 'POST':
        src = request.form['source']
        dest = request.form['destination']

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM flights WHERE source=? AND destination=?", (src, dest))
        flights = c.fetchall()
        conn.close()

    return render_template('search.html', flights=flights)

@app.route('/book/<int:id>', methods=['GET','POST'])
def book(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM flights WHERE id=?", (id,))
    flight = c.fetchone()

    if request.method == 'POST':
        name = request.form['name']

        c.execute("INSERT INTO bookings(passenger,flight,route,price) VALUES(?,?,?,?)",
                  (name, flight[1], flight[2]+"-"+flight[3], flight[6]))
        conn.commit()

        booking_id = c.lastrowid
        conn.close()

        return redirect(f'/ticket/{booking_id}')

    conn.close()
    return render_template('book.html', flight=flight)

@app.route('/ticket/<int:id>')
def ticket(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM bookings WHERE id=?", (id,))
    booking = c.fetchone()
    conn.close()

    return render_template('ticket.html', booking=booking)

if __name__ == "__main__":
    app.run(debug=True)
