import sys

import pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def fetch_data_from_mysql():
    # 连接数据库
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='99221',
                                 db='pyqt')

    try:
        with connection.cursor() as cursor:
            # 执行SQL查询
            cursor.execute(
                "SELECT vdot "
                "FROM vdot "
                "WHERE TIME_TO_SEC(distance_3km) > TIME_TO_SEC('00:09:30')"
                "ORDER BY TIME_TO_SEC(distance_3km)"
                " LIMIT 1; ")
            result = cursor.fetchone()
            return result[0] if result else "No data found"
    finally:
        connection.close()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MySQL Data Display')
        self.setGeometry(100, 100, 800, 600)

        # 创建Label用于显示数据
        self.data_label = QLabel(self)
        self.data_label.move(500, 500)
        self.data_label.setStyleSheet("font-size: 16px;")

        self.show_data()

    def show_data(self):
        data = fetch_data_from_mysql()
        self.data_label.setText(str(data))

    # 实例化并运行应用


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
