import sys
import random

from PyQt6.QtWidgets import QWidget, QApplication, QSlider, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage, QColor, QTransform, QPainter, QPen, QBrush
from PyQt6.QtCore import QRectF, Qt
from PyQt6 import uic

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.pushButton = QPushButton("Нарисовать")
        self.layout.addWidget(self.pushButton)
        self.setLayout(self.layout) 
        self.setFixedSize(600, 500) 
        self.setWindowTitle("Good Mood Rising Programmatic UI")

class GoodMoodRising(window):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.color = QColor(
                random.randrange(0, 256),
                random.randrange(0, 256),
                random.randrange(0, 256)
            )
        qp.setPen(self.color)
        m_s = min(self.width(), self.height()) // 2
        s = random.randrange(20, m_s) 
        x = random.randrange(2, self.width() - s)
        y = random.randrange(2, self.height() - s)
        rect1 = QRectF(x, y, s, s )
        qp.setBrush(QBrush(self.color, Qt.BrushStyle.SolidPattern))
        qp.drawEllipse(rect1)
        self.color = QColor(
                random.randrange(0, 256),
                random.randrange(0, 256),
                random.randrange(0, 256)
            )
        qp.setPen(self.color)
        qp.setBrush(QBrush(self.color, Qt.BrushStyle.SolidPattern))
        s = random.randrange(20, m_s) 
        x = random.randrange(2, self.width() - s)
        y = random.randrange(2, self.height() - s)
        rect2 = QRectF(x, y, s, s )
        qp.drawEllipse(rect2)
        self.color = QColor(
                random.randrange(0, 256),
                random.randrange(0, 256),
                random.randrange(0, 256)
            )
        qp.setPen(self.color)
        qp.setBrush(QBrush(self.color, Qt.BrushStyle.SolidPattern))
        s = random.randrange(20, m_s) 
        x = random.randrange(2, self.width() - s)
        y = random.randrange(2, self.height() - s)
        rect3 = QRectF(x, y, s, s )
        qp.drawEllipse(rect3)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())