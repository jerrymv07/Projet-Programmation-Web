from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    nom = request.form.get("nom")
    email = request.form.get("email")
    message = request.form.get("message")
    return f"Merci {nom} ! Nous avons reçu votre message : {message} ({email})"

contacts = []  # liste temporaire

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/add_contact", methods=["POST"])
def add_contact():
    nom = request.form.get("nom")
    email = request.form.get("email")

    contacts.append({"nom": nom, "email": email})

@app.route("/contacts")
def afficher_contacts():
    return render_template("contacts.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)