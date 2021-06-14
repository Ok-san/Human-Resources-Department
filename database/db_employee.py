import sqlite3


class DataBaseEmpoyee:
    # соединение с базой данных
    connection = sqlite3.connect('database/employee.db')
    # подключение для создания запросов
    cur = connection.cursor()

    def displayDataBase(self):
        # запрос вывода всех данных
        self.cur.execute("SELECT * FROM employee;")
        result = self.cur.fetchall()
        return result

    def addingDataBase(self):
        # запрос добавления
        self.cur.execute("INSERT INTO employee")
        self.connection.commit()

    def changingDataBase(self):
        # запрос изменения
        self.cur.execute("")
        self.connection.commit()

    def deleteData(self):
        # запрос удаления
        self.cur.execute("DELETE FROM employee")
        self.connection.commit()

    def searchDataBase(self):
        # запрос поиска
        self.cur.execute("")
        self.connection.commit()
