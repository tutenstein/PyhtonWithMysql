import mysql.connector
import pandas as pd
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

def exportProductlistTocsv(list):
    product_data = {
        'id': [],
        'name': [],
        'price': [],
        'imageUrl': [],
        'description': []
    }
    for a in list:
        product_data['id'].append(a[0])
        product_data['name'].append(a[1])
        product_data['price'].append(a[2])
        product_data['imageUrl'].append(a[3])
        product_data['description'].append(a[4])


    data = pd.DataFrame(product_data)
    data.to_csv("products.csv")
    print("Data exported in csv format")

def getProducts():
    cursor = connection.cursor()
    cursor.execute('SELECT * From products')
    return cursor.fetchall()


for products in getProducts():
    print(f'name: {products[1]} price: {products[2]}')

exportProductlistTocsv(getProducts())
