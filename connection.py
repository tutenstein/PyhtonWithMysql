import mysql.connector

connection = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root_passw",
    database="node-app"
)
