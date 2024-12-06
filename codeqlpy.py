import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
#
##db_config = {
    ##'host': 'localhost',
    ##'user': 'root',
    ##'password': 'aisin4AiLien',
    ##'database': 'codeql_schema'
##}

app = Flask(name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connection configuration with a hardcoded password
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="aisin4AiLien",  # <-- Hardcoded password used in an external sink
                database="codeql_schema"
            )
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS form_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    message TEXT NOT NULL
                )
            ''')
            # Insert form data into the database
            cursor.execute('''
                INSERT INTO form_data (name, email, message)
                VALUES (%s, %s, %s)
            ''', (name, email, message))
            conn.commit()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('success'))

    return render_template('form.html')

@app.route('/success')
def success():
    return "Form submitted successfully and stored in the database!"

if name == 'main':
    app.run(debug=True)
