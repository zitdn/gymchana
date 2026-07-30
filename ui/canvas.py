from PySide6.QtWidgets import QWidget, QPainter


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        pass

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fill
