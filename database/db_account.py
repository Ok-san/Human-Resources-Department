import sqlite3


class DataBaseAccount:
    connection = sqlite3.connect('./account.db')
    cur = connection.cursor()

    def checkUsernameAndPassword(self):
        self.cur.execute("SELECT * FROM account;")
        result = self.cur.fetchall()
        return result
