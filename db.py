import sqlite3 as sq3

con = sq3.connect("database.db", check_same_thread=False)
print("connected to DB")
cur = con.cursor()

# Создание таблицы и ее параметры
cur.execute("""CREATE TABLE IF NOT EXISTS data(
   id INT PRIMARY KEY,
   resource TEXT,
   email TEXT,
   login_nick TEXT,
   password TEXT);
""")
con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS maspass (
    key TEXT);
""")
con.commit()








max_id = cur.execute("SELECT max(id) FROM data").fetchone()[0]
if max_id == None:
        max_id = 0

def get_last_id_p1():
    try:
        return cur.execute("SELECT max(id) FROM data").fetchone()[0] + 1
    except:
        return 1

def get_all_data():

    '''Возвращает список всех записей из таблицы data'''

    cur.execute("SELECT * FROM data")
    return cur.fetchall()

def get_unique():
    '''Возвращает все значения без повторений'''

    cur.execute("SELECT DISTINCT resource FROM data")
    names = cur.fetchall()
    return names

def add_to_base(max_id, data):
    '''Добавляет в таблицу данные из переданного спсика'''
    print(max_id)
    cur.execute("INSERT OR IGNORE INTO data VALUES(?, ?, ?, ?, ?);", (str(max_id), data[0], data[1], data[2], data[3]))
    con.commit()
    # print("added")
    # print(cur.execute("SELECT * FROM data").fetchall())

def delete_from_base(id):
     cur.execute(f"DELETE FROM data WHERE id={id}")
     con.commit()
     

def get_records_from_res(res: str):
    cur.execute(f"SELECT * FROM data WHERE resource = '{res}'")
    length = cur.fetchall() 
    return length, len(length)

def get_key():
     cur.execute("SELECT * FROM maspass")
     try:
          return cur.fetchall()[0][0]
     except:
        return cur.fetchall()

def update_key(data):
     print(data)
     cur.execute(f"UPDATE maspass SET key='{data}'")
     con.commit()
     print('commited')

if get_key() == []:
    cur.execute("""INSERT OR IGNORE INTO maspass values (0) """)
    con.commit()

# uniques = [r[0] for r in get_unique()]

# cur.execute("DELETE FROM data WHERE id = '2' ")

# print(get_unique())

if __name__ == "__main__":
    # cur.execute("INSERT INTO maspass VALUES(0);")
    # con.commit()
    print(get_key())


