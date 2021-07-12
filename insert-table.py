import mysql.connector
from connection import connection

def insertProducts(list):
    cursor = connection.cursor()
    sql = 'INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} registration added ')
    except mysql.connector.Error as err:
        print('Error: ',err)
    finally:
        connection.close()
        print("Database connection closed.")

list = []
while True:
    name = input('product Name: ')
    price = float(input('Product price: '))
    imageUrl = input('Product image url: ')
    description = input('Product description: ')
    list.append((name,price,imageUrl,description))
    result = input("do you want to continue(y/n)? ")
    if result == 'h':
        print('your registrations are being added to the database...')
        insertProducts(list)
        break


