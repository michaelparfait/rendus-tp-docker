import os
from typing import List
from flask import Flask, request, render_template
from mysql.connector import MySQLConnection, Error
# from databaseconfig import read_db_config
import json

template_dir = os.path.abspath('../../templates')

app = Flask(__name__, template_folder='/TP/exo3/templates')

users = []

def getusers() -> List:

    # connection = mysql.connector.connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])

    connection =connect_database()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    results = [{id: name} for (id, name) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/ws/v1/users')
def get_users() -> str:
    return json.dumps(getusers())


# GET and POST requests
@app.route('/ws/v1/user', methods=['GET', 'POST'])
def add_get_user():

    if request.method == 'POST':
         name = request.form.get('name')
         users.append(name)
         insert_user(users)

         return '''
                  <h1>Votre nom est : {}</h1>'''.format(name)
    
    # render_template('user.html')
    return '''
              <form action="/ws/v1/user" method="POST">
                  <div><label>Name: <input type = "text" name = "name" placeholder="name" required/></label></div>
                  <button type="submit" class="btn btn-default">Submit</button>
              </form>'''


def insert_user(user):
    query = "INSERT INTO user(id, name) VALUES(NULL, %s);"
    

    try:
        # connection = mysql.connector.connect(cfg.mysql["host"], cfg.mysql["user"], cfg.mysql["password"])

        connection = connect_database()

        cursor = connection.cursor()
        cursor.execute(query, user)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        connection.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        connection.close()

def connect_database():
    config = {
        'user': 'root',
        'password': 'password',
        'host': 'mysql-db',
        'port': '3306',
        'database': 'docker'
    }
    return MySQLConnection(**config)


if __name__ == '__main__':
    app.run(host='0.0.0.0')