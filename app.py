from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)


db_config = {
    'host': 'localhost',
    'user': 'note_user',      
    'password': 'Password123!', 
    'database': 'notes_db'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            query = "INSERT INTO notes (content, created_at) VALUES (%s, %s)"
            cursor.execute(query, (content, datetime.now()))
            conn.commit()
        return redirect('/')

    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)