# db.py
import os
import pymysql
from flask import jsonify


db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        #  if os.environ.get('GAE_ENV') == 'standard':
        conn = pymysql.connect(user=db_user, password=db_password, unix_socket=unix_socket,
                               db=db_name, cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_producer():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM producer;')
        producer = cursor.fetchall()
        if result > 0:
            got_producer = jsonify({'results': producer})
        else:
            got_producer = 'No products in DB'
    conn.close()
    return got_producer


def get_producer_detail(producer_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute(
            'SELECT * FROM producer WHERE producer_id=%s;', (producer_id))
        producer_detail = cursor.fetchone()
        if result > 0:
            got_producer = jsonify(producer_detail)
        else:
            got_producer = 'No producer in DB'
    conn.close()
    return got_producer
