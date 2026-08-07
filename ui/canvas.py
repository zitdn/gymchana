from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt, Signal


class Canvas(QWidget):
    mouse_pressed = Signal(int, int)
    mouse_moved = Signal(int, int)
    mouse_released = Signal()
    def __init__(self, track, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.track = track

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        for obj in self.track.objects:
            obj.draw(painter)

        painter.end()

    def mouseMoveEvent(self, event):
        x_cursor = event.x()
        y_cursor = event.y()
        self.mouse_moved.emit(x_cursor, y_cursor)

    def mousePressEvent(self, event):
        x_cursor = event.x()
        y_cursor = event.y()
        
        self.mouse_pressed.emit(x_cursor, y_cursor)
        
            
        

    def mouseReleaseEvent(self, event):
        self.mouse_released.emit()