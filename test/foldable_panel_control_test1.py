import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolButton, QTextEdit


class CollapsiblePanel(QWidget):
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.title_text = title
        self.content_widget = QTextEdit()
        self.content_widget.setReadOnly(True)
        self.content_widget.hide()

        self.toggle_button = QToolButton(self)
        self.toggle_button.setText(self.title_text)
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.RightArrow)
        self.toggle_button.pressed.connect(self.on_toggle)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.content_widget)

    def on_toggle(self):
        if self.content_widget.isHidden():
            self.content_widget.show()
            self.toggle_button.setArrowType(Qt.DownArrow)
        else:
            self.content_widget.hide()
            self.toggle_button.setArrowType(Qt.RightArrow)

    def setContent(self, content):
        self.content_widget.setPlainText(content)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        panel1 = CollapsiblePanel("标题1")
        panel1.setContent("这里是标题1的详细信息。\n可以是多行文本。")
        layout.addWidget(panel1)

        panel2 = CollapsiblePanel("标题2")
        panel2.setContent("这里是标题2的详细信息。\n可以包含各种控件。")
        layout.addWidget(panel2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
