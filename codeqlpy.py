import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'aisin4AiLien',
    'database': 'codeql_schema'
}
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connexion à la base de données et insertion des données
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Créer la table si elle n'existe pas
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS form_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    message TEXT NOT NULL
                )
            ''')
            # Insérer les données du formulaire
            cursor.execute('''
                INSERT INTO form_data (name, email, message)
                VALUES (%s, %s, %s)
            ''', (name, email, message))
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Erreur MySQL : {err}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('success'))

    return render_template('form.html')

# Route pour afficher un message de succès
@app.route('/success')
def success():
    return "Formulaire soumis avec succès et enregistré dans la base de données !"

if __name__ == '__main__':
    app.run(debug=True)