import mysql.connector 
mydb = mysql.connector.connect(     #just for less typing
  host="localhost",       #connects you to the mysqlinstance i think
  user="root",
  password="root"
)
mycursor = mydb.cursor()   #just for less typing
mycursor.execute("CREATE DATABASE IF NOT EXISTS leaderboard")
mycursor.execute("USE leaderboard")  #which database to use
mycursor.execute("CREATE TABLE IF NOT EXISTS players (name1 VARCHAR(255), wins INT DEFAULT 0, draws INT DEFAULT 0, loses INT DEFAULT 0)")

