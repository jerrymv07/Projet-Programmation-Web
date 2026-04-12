
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -----------------------------
# Connexion base de données
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect('contacts.db')
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# Initialisation DB
# -----------------------------
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            telephone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# READ - afficher contacts
# -----------------------------
@app.route('/')
def index():
    conn = get_db_connection()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

# -----------------------------
# CREATE - ajouter contact
# -----------------------------
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO contacts (nom, prenom, telephone, email) VALUES (?, ?, ?, ?)',
            (nom, prenom, telephone, email)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('add.html')

# -----------------------------
# UPDATE - modifier contact
# -----------------------------
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    contact = conn.execute('SELECT * FROM contacts WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        telephone = request.form['telephone']
        email = request.form['email']

        conn.execute(
            'UPDATE contacts SET nom=?, prenom=?, telephone=?, email=? WHERE id=?',
            (nom, prenom, telephone, email, id)
        )
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('edit.html', contact=contact)

# -----------------------------
# DELETE - supprimer contact
# -----------------------------


@app.route('/delete/<int:id>', methods=('GET', 'POST'))
def delete(id):
    conn = get_db_connection()
    contact = conn.execute('SELECT * FROM contacts WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        conn.execute('DELETE FROM contacts WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('delete.html', contact=contact)

#VOIR LES DETAILS D'UN CONTACT

@app.route('/view/<int:id>')
def view(id):
    conn = get_db_connection()
    contact = conn.execute('SELECT * FROM contacts WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('view.html', contact=contact)


#retour a la page d'acceuil
@app.route('/home')
def home():
    return redirect('/')

# -----------------------------
# Lancer l'application
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)

