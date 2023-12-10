import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_Form


class Window(QWidget, Ui_Form):
    '''Класс окна программы'''

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        '''Метод предназначен для работы QPainter'''
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        '''Слот реализует работу кнопки self.pushButton'''
        self.do_paint = True
        self.update()

    def drawCircle(self, qp):
        '''Метод рисует окружности при нажатии self.pushButton'''
        qp.setBrush(QColor(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255)))
        x = random.randint(0, 509)
        y = random.randint(0, 509)
        size = random.randint(0, 250)
        x2 = x + size
        y2 = x + size
        qp.drawEllipse(x, y, x2, y2)


app = QApplication(sys.argv)
if __name__ == '__main__':
    ex = Window()
    ex.show()
    sys.exit(app.exec())
