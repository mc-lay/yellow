import random
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QCursor, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.draw_circles)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_circles(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        x = random.randint(30, 150)
        y = random.randint(30, 150)
        for i in range(random.randint(1, 7)):
            diameter = random.randint(30, 100)
            x += 20
            y += 20
            qp.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
