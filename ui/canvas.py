from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class Canvas(QWidget):
    def __init__(self, mouse_callback, parent=None ):
        super().__init__(parent)
        self.setMouseTracking(True)

        self.mouse_callback = mouse_callback

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)

        painter.end()

    def mouseMoveEvent(self, event):
        x_cursor = event.x()
        y_cursor = event.y()

        self.mouse_callback(x_cursor, y_cursor )