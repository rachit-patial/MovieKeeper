import sqlite3

def connect():
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movie(id INTEGER PRIMARY KEY, mov_name TEXT, actor_name TEXT, year INTEGER, location TEXT)")
    conn.commit()
    conn.close()

def insert(mov_name, actor_name, year, loc):
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO movie VALUES(NULL,?,?,?,?)",(mov_name, actor_name, year, loc))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(mov_name= "", actor_name="", year="", loc=""):
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM movie WHERE mov_name = ? OR actor_name = ? OR year = ? OR location = ?", (mov_name, actor_name, year, loc))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM movie WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, mov_name, actor_name, year, loc):
    conn = sqlite3.connect("movie.db")
    cur = conn.cursor()
    cur.execute("UPDATE movie SET mov_name = ?, actor_name = ?, year = ?, location = ? WHERE id = ?",(mov_name, actor_name, year, loc, id))
    conn.commit()
    conn.close()

connect()
#insert("MoneyBall", "Brad", 2011, "E:\movies\Moneyball (2011) 720p BluRay x264 - 800MB - YIFY")
#update(2,"MoneyBall", "Brad Pitt", 2011, "E:\movies\Moneyball (2011) 720p BluRay x264 - 800MB - YIFY")
#print(search(mov_name="MoneyBall"))
#print(view())
#delete(3)