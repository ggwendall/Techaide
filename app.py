from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données MySQL
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "example",
    "database": "techaide",
    "port": 3307,
}

# Route pour afficher la page d'accueil
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route pour afficher le formulaire
@app.route("/donate", methods=["GET"])
def donate():
    return render_template("donate.html")

# Route pour soumettre le formulaire
@app.route("/submit_donation", methods=["POST"])
def submit_donation():
    if request.method == "POST":
        fname = request.form["fname"]
        email = request.form["email"]
        amount = float(request.form["amount"])  # Convertir en float car c'est un montant
        message = request.form["message"]

        # Insérer les données dans la base de données MySQL
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Exécutez votre requête SQL d'insertion ici
            query = "INSERT INTO donations (fname, email, amount, message) VALUES (%s, %s, %s, %s)"
            values = (fname, email, amount, message)
            cursor.execute(query, values)

            connection.commit()
            cursor.close()
            connection.close()

            # Rediriger vers une page de confirmation ou d'accusé de réception
            return "Merci pour votre donation !"

        except Exception as e:
            return f"Une erreur est survenue : {e}"

if __name__ == "__main__":
    app.run()
