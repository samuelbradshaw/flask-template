# Third-party libraries
import mysql.connector

# Internal imports
from main import config


conn = None
def connect_db():
  global conn
  if conn is not None:
    try:
      assert conn.is_connected()
    except:
      conn = None
  if conn is None:
    conn = mysql.connector.connect(host=config.DBInfo.SERVER, user=config.DBInfo.USERNAME, password=config.DBInfo.PASSWORD, db=config.DBInfo.DATABASE, charset='utf8', use_unicode=True, port=config.DBInfo.PORT, get_warnings=True)
  return conn

def close_connection():
  if conn is not None:
    conn.close()

def lookup(sql, *args):
#   print(sql)
#   print(args)
  connection = connect_db()
  cursor = connection.cursor(dictionary=True)
  cursor.execute(sql, args)
  rows = cursor.fetchall()
  cursor.close()
  return rows

def lookup_one(sql, *args):
  connection = connect_db()
  cursor = connection.cursor(dictionary=True)
  cursor.execute(sql, args)
  row = cursor.fetchone()
  cursor.close()
  return row

def update(sql, *args):
  connection = connect_db()
  cursor = connection.cursor(dictionary=True)
  cursor.execute(sql, args)
  row_count = cursor.rowcount
  last_row_id = cursor.lastrowid
  warnings = cursor.fetchwarnings()
  conn.commit()
  cursor.close()
  return { 'row_count': row_count, 'last_row_id': last_row_id, 'warnings': warnings }
