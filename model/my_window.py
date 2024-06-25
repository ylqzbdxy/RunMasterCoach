from PyQt5.QtWidgets import QMainWindow

from gui.main_window import Ui_MainWindow


class myWindow(QMainWindow, Ui_MainWindow):
    """
    主窗口类，负责界面初始化及按钮事件处理。
    """

    def __init__(self):
        """
        初始化主窗口，加载界面布局。
        """
        super().__init__()
        self.setupUi(self)
        self._initializePageChangeFunctions()
        self._connectSignals()

    def setupUi(self, MainWindow):
        super().setupUi(self)
        # self.setTextEditDisplay(False)
        # self.toolButton.clicked.connect(self.on_toggle_clicked)
        # self.contentWidget.setVisible(False)

    def _initializePageChangeFunctions(self):
        """
        初始化页面切换的辅助函数列表。
        """
        self.pageChangeFunctions = [
            self.btnHome, self.btnCalc, self.btnPlan,
            self.btnMovement, self.btnPrevent, self.btnConversaion,
            self.btnForecast1, self.btnForecast2
        ]

    def _connectSignals(self):
        """
        连接所有按钮的点击信号到相应的槽函数。
        """
        buttons = [
            self.pushButton_home, self.pushButton_clac,
            self.pushButton_plan, self.pushButton_movement,
            self.pushButton_prevent, self.pushButton_conversaion,
            self.pushButton_forecast
        ]
        for button, func in zip(buttons, self.pageChangeFunctions):
            button.clicked.connect(func)

    # def setTextEditDisplay(self, is_display):
    #     self.textEdit.setVisible(is_display)
    #
    # def on_toggle_clicked(self):
    #     if self.textEdit.isVisible():
    #         self.setTextEditDisplay(False)
    #     else:
    #         self.setTextEditDisplay(True)

    def setPage(self, index):
        """
        根据索引设置当前显示的页面。
        """
        self.stackedWidget.setCurrentIndex(index)

    def btnHome(self):
        self.setPage(0)

    def btnCalc(self):
        self.setPage(1)

    def btnPlan(self):
        self.setPage(2)

    def btnMovement(self):
        self.setPage(3)

    def btnPrevent(self):
        self.setPage(4)

    def btnConversaion(self):
        self.setPage(5)

    def btnForecast1(self):
        self.setPage(6)

    def btnForecast2(self):
        self.setPage(7)
