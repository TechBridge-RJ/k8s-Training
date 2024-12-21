from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
CORS(app)

dbTable = os.environ['dbTable']
dbHost = os.environ['dbHost']
dbName = os.environ['dbName']
dbUser = os.environ['dbUser']
dbPass = os.environ['dbPass']

db_config = {
    'host': dbHost,        # Host where MySQL is running 192.168.0.22
    'database': dbName,  # Name of your database demo_mysql
    'user': dbUser,          # MySQL username mysql-admin
    'password': dbPass   # MySQL password mysql-password
}

# Function to append new user feedback data to the 'users_feedback' table
def append_feedback(name, feedback):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)        
        
        if connection.is_connected():
            print("connection successful")
            cursor = connection.cursor()

            # Perform a query
            sqlStatemet = "SELECT * FROM "+dbTable
            cursor.execute(sqlStatemet)
            result = cursor.fetchall()

            # Define the SQL INSERT query
            sql_insert_query ="INSERT INTO "+dbTable+" (name, feedback) VALUES (%s, %s)"
            
            # asdData to be appended (name and email)
            data = (name, feedback)
            
            # Execute the SQL query
            cursor.execute(sql_insert_query,data)
            
            # Commit the changes to the database
            connection.commit()
            
            print(f"New user feedback added successfully: {name} - {feedback}")
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

def get_data():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)
        
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Use dictionary=True for JSON serializable output

            sql_get_query = "SELECT * FROM "+dbTable
            # Execute a query
            #cursor.execute("SELECT * FROM users_feedback")
            data = (dbTable)
            cursor.execute(sql_get_query)
            results = cursor.fetchall()
            reversed_results = results[::-1]

            # Return results as JSON
            return {'status':'successful','table':reversed_results}

    except mysql.connector.Error as err:
        return {'status':'failed'}

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()



@app.route('/api/feedback', methods=['GET','POST'])
def feedback():
    # Get container name
    with open('/etc/hostname', 'r') as f:
        container_id = f.read().strip()

    # Process post request
    if request.method == 'POST':
        dataPost = request.get_json()
        feedback = dataPost['feedback']
        user = dataPost['user']

        try:
            append_feedback(user, feedback)
            response = "status : successful user : "+user+" feedback : "+feedback
            data = {
                "container_id": container_id,
                "response": response
            }
        except:
            response = "status : failed user : "+user+" feedback : "+feedback
            data = {
                "container_id": container_id,
                "response": response
            }
        return data
    # Process get request
    if request.method == 'GET':
        dictData = {}
        dictData['container_id'] = container_id
        dictData['data'] = get_data()

        return jsonify(dictData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)