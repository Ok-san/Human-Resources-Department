from database.db_employee import DataBaseEmpoyee
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from autorisation import *
from mainwindow import *
from interface import *
from display import *
from check import *


class Controller(QtWidgets.QWidget):

    m_Interface = Interface()
    m_Display = Display()
    m_Check = Check()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AutorisationWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit_2, self.ui.lineEdit_3]

    def auth(self):
        if(self.m_Check.checkInput(self.base_line_edit) == 0):
            QtWidgets.QMessageBox.warning(
                self, 'Предупреждение', 'Пожалуйста, введите все необходимые данные!')
        elif (self.m_Check.cheсkLoginAndPassword(self.base_line_edit) == 0):
            QtWidgets.QMessageBox.warning(
                self, 'Ошибка', 'Введен не верный логин или пароль! Попробуйте снова')
        else:
            self.hide()
            self.window = QtWidgets.QWidget()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.database = DataBaseEmpoyee()
            self.result = self.database.displayDataBase()
            rows = len(self.result)
            columns = len(self.result[0])
            self.tab(columns, rows, self.result)

    def tab(self, columns, rows, results):
        self.ui.tableWidget.setRowCount(rows)
        self.ui.tableWidget.setColumnCount(columns)
        for i in range(rows):
            for j in range(columns):
                item = QTableWidgetItem("{}".format(results[i][j]))

                self.ui.tableWidget.setItem(i, j, item)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Controller()
    mywin.show()
    sys.exit(app.exec_())
