# from donut import Donut

from decouple import config
import mysql.connector
from mysql.connector.cursor import MySQLCursor



def main():
    # Connect to MySQL database

    db_mysql = mysql.connector.connect(user=config("MYSQL_DATABASE_USER"), 
                             password=config("MYSQL_DATABASE_PASSWORD"), 
                             host=config("MYSQL_DATABASE_HOST"), 
                             database=config("MYSQL_DATABASE_DB"))

    # create cursor to MySQL database to use stored procedures or execute queries
    cursor = db_mysql.cursor()

    cursor.execute("SELECT * FROM donuts")
    portfolio = cursor.fetchall()
   
    print('Available donuts: ')
    print(portfolio)

    
if __name__ == '__main__':
    main()