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

            # Afficher un message de remerciement avec les styles spécifiques
            return """
            
                <html>
                <head>
                    <link rel="stylesheet" href="static\css\submit-donation.css">
                </head>
                <body class="submit-donation-page">
                    <div class="thank-you-message">
                        <h2>Merci pour votre donation !</h2>
                        <p>Nous vous sommes très reconnaissants pour votre générosité.</p>
                    </div>
                </body>
                </html>
            """

        except Exception as e:
            return f"Une erreur est survenue : {e}"


@app.route("/donate_list", methods=["GET"])
def donate_list():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Exécutez votre requête SQL pour récupérer la liste des dons
        query = "SELECT * FROM donations"
        cursor.execute(query)
        donations = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template("donate_list.html", donations=donations)

    except Exception as e:
        return f"Une erreur est survenue : {e}"


if __name__ == "__main__":
    app.run()
