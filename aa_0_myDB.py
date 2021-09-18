import sqlite3


def insertOrReplaceStationData(time, port, num_pack, message):

    conn = sqlite3.connect("report.db")
    cur = conn.cursor()

    cmd = """
           CREATE TABLE IF NOT EXISTS report (
               time TEXT,
               port TEXT,
               num_pack INT,
               message TEXT
           );
           """
    cur.execute(cmd)

    cmd = "INSERT OR REPLACE INTO report VALUES(?, ?, ?, ?)"

    cur.execute(cmd, (time, port, num_pack, message))
    conn.commit()
    conn.close()


if __name__== "__main__":
    insertOrReplaceStationData("09/15/21, 12:41:43", "fgfgfggfgfgfgf", 5, "rrrr")