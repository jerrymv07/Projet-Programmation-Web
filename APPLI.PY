from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = []
next_id = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/CONTACT")
def CONTACT():
    return render_template("CONTACT.html")

@app.route("/add_contact", methods=["POST"])
def add_contact():
    global next_id

    nom = request.form.get("nom")
    email = request.form.get("email")

    contacts.append({
        "id": next_id,
        "nom": nom,
        "email": email
    })

    next_id += 1

    return redirect(url_for('afficher_contacts'))

@app.route("/contacts")
def afficher_contacts():
    return render_template("contacts.html", contacts=contacts)

@app.route("/edit/<int:id>")
def edit_contact(id):
    contact = None

    for c in contacts:
        if c["id"] == id:
            contact = c
            break

    return render_template("edit_contact.html", contact=contact)

@app.route("/update/<int:id>", methods=["POST"])
def update_contact(id):
    for c in contacts:
        if c["id"] == id:
            c["nom"] = request.form.get("nom")
            c["email"] = request.form.get("email")
            break

    return redirect(url_for('afficher_contacts'))

if __name__ == "__main__":
    app.run(debug=True)