from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class Canvas(QWidget):
    def __init__(self, track, mouse_move_callback, mouse_click_callback, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.dragging = False
        self.drag_obj = None
        self.track = track
        self.mouse_move_callback = mouse_move_callback
        self.mouse_click_callback = mouse_click_callback

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)
        for cone in self.track.cones:
            cone.draw(painter)

        print(len(self.track.cones))
        painter.end()

    def mouseMoveEvent(self, event):
        x_cursor = event.x()
        y_cursor = event.y()
        if self.dragging and self.drag_obj:
            self.drag_obj.move_to(x_cursor, y_cursor)
            self.update()

        self.mouse_move_callback(x_cursor, y_cursor)

    def mousePressEvent(self, event):
        x_cursor = event.x()
        y_cursor = event.y()
        obj = self.mouse_click_callback(x_cursor,y_cursor)
        if obj:
            self.drag_obj = obj
            self.dragging = True
        

    def mouseReleaseEvent(self, event):
        self.drag_obj = None
        self.dragging = False