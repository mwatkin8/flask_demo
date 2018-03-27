import sqlite3, os

def create_table(db_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

def pull_from_db():
    with sqlite3.connect("therapy.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM Patient")
        rows = cursor.fetchall()
        val = str(rows)
    return val

def insert_to_db():
    demographics = [("P123", "Johnny", 25, "12/1/92", "M")]
    with sqlite3.connect("therapy.db") as db:
        cursor = db.cursor()
        sql = "insert into Patient (ID, name, age, birthday, gender) values (?,?,?,?,?)"
        cursor.executemany(sql, demographics)
        db.commit()

def run(db_name):
    sql = """create table Patient
            (ID text,
            name text,
            age integer,
            birthday text,
            gender text)"""

    if not os.path.isfile("therapy.db"):
        create_table(db_name, sql)
    insert_to_db()
    return pull_from_db()
