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

if __name__ == "__main__":
    app.run(debug=True)