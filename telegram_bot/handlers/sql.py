import sqlite3 as sql
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB = BASE_DIR/'db.sqlite3'

def update(user_id, apples=0, moneys=0, health=0, level=0, inventory=False, weapon=False):
    """
    Писать на сколько увеличить что то или заменить текст
    :param user_id:
    :param apples:
    :param moneys:
    :param health:
    :param level:
    :param inventory:
    :param weapon:
    :return:
    """
    with sql.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
        user_data = list(cur.fetchone())
        print(user_data)
        user_data[3] += apples
        user_data[4] += moneys
        user_data[5] += health
        user_data[6] += level
        if inventory:
            user_data[7] += inventory
        if weapon:
            user_data[8] = weapon
        cur.execute('DELETE FROM users WHERE user_id=?', (user_id,))
        print(user_data)
        cur.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', user_data)
    return user_data
