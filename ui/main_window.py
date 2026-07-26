from PySide6.QtWidgets import QMainWindow, QToolBar, QLabel
from PySide6.QtGui import QAction


x_cursor = 0
y_cursor = 0
cone_count = 0
zoom = 100


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.create_actions()
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_status_bar()
        
        
    def setup_ui(self):
        self.resize(1400, 900)
        self.setMinimumSize(900, 600)
        self.setWindowTitle('Gymkhana Designer')

    def create_actions(self):
        # Файл
        self.action_new = QAction("Создать", self)
        self.action_open = QAction('Открыть', self)
        self.action_save = QAction('Сохранить', self)
        self.action_save_as = QAction('Сохранить как...', self)
        self.action_exit = QAction('Выход', self)
        # Правка
        self.action_undo = QAction("Отменить", self)
        self.action_redo = QAction('Повторить', self)
        # Вид
        self.action_zoom_reset = QAction("Масштаб 100%", self)
        self.action_zoom_in = QAction('Приблизить', self)
        self.action_zoom_out = QAction('Отдалить', self)
        # Инструменты
        self.action_cone = QAction("Конус", self) 
        self.action_line = QAction('Линия', self)
        self.action_arc = QAction('Дуга', self)
        # Помощь
        self.action_about = QAction("О программе", self)

    def create_menu_bar(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('Файл')
        file_menu.addAction(self.action_new)
        file_menu.addAction(self.action_open)
        file_menu.addAction(self.action_save)
        file_menu.addAction(self.action_save_as)
        file_menu.addSeparator()
        file_menu.addAction(self.action_exit)

        edit_menu = menu.addMenu('Правка')
        edit_menu.addAction(self.action_undo)
        edit_menu.addAction(self.action_redo)

        view_menu = menu.addMenu('Вид')
        view_menu.addAction(self.action_zoom_reset)
        view_menu.addAction(self.action_zoom_in)
        view_menu.addAction(self.action_zoom_out)
       
        tools_menu = menu.addMenu('Инструменты')
        tools_menu.addAction(self.action_cone) 
        tools_menu.addAction(self.action_line)
        tools_menu.addAction(self.action_arc)

        help_menu = menu.addMenu('Помощь')
        help_menu.addAction(self.action_about)

    def create_tool_bar(self):
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.action_new)
        self.toolbar.addAction(self.action_open)
        self.toolbar.addAction(self.action_save)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_cone)
        self.toolbar.addAction(self.action_line)
        self.toolbar.addAction(self.action_arc)

    def create_status_bar(self):
        self.statusbar = self.statusBar()
        self.x_label = QLabel(f'x: {x_cursor}', self)
        self.y_label = QLabel(f'y: {y_cursor}', self)
        self.zoom_label = QLabel(f'Масштаб: {zoom}%', self)
        self.cone_label = QLabel(f'Конусов: {cone_count}', self)
        self.statusbar.addPermanentWidget(self.x_label)
        self.statusbar.addPermanentWidget(self.y_label)
        self.statusbar.addPermanentWidget(self.zoom_label)
        self.statusbar.addPermanentWidget(self.cone_label)