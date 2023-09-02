import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = open("C:\\Users\\user\\desktop\\fsdevroadmap\\backend\\frameworks\\django\\dcrm\\dcrm\\db_password", "r").read()

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

print("All Done!")
