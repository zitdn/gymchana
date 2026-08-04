from PySide6.QtWidgets import QMainWindow, QToolBar, QLabel
from PySide6.QtGui import QAction
from ui.canvas import Canvas
from models.track import Track
from models.cone import Cone
from models.tools import Tool


zoom = 100


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_cone = None
        self.current_tool = Tool.SELECT
        self.track = Track()
        self.setup_ui()
        self.create_actions()
        self.connect_actions()
        self.create_menu_bar()
        self.create_tool_bar()
        self.create_status_bar()
        self.create_canvas()
        

        
        
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
        self.action_select = QAction("Выбор", self)
        self.action_cone = QAction("Конус", self) 
        self.action_line = QAction('Линия', self)
        self.action_arc = QAction('Дуга', self)
        # Помощь
        self.action_about = QAction("О программе", self)

    def connect_actions(self):
        self.action_select.triggered.connect(
            lambda : self.set_tool(Tool.SELECT)
        )
        self.action_cone.triggered.connect(
            lambda : self.set_tool(Tool.CONE)
        )
        self.action_line.triggered.connect(
            lambda : self.set_tool(Tool.LINE)
        )
        self.action_arc.triggered.connect(
            lambda : self.set_tool(Tool.ARC) 
        )

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
        tools_menu.addAction(self.action_select)
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
        self.toolbar.addAction(self.action_select)
        self.toolbar.addAction(self.action_cone)
        self.toolbar.addAction(self.action_line)
        self.toolbar.addAction(self.action_arc)

    def update_coordinates(self, x, y):
        self.x_label.setText(f'x: {x}')
        self.y_label.setText(f'y: {y}')       

    def set_tool(self, tool):
        self.current_tool = tool
        if self.current_tool == Tool.CONE:
            self.tool_label.setText('Инструмент: Конус')
        elif self.current_tool == Tool.LINE:
            self.tool_label.setText('Инструмент: Линия')
        elif self.current_tool == Tool.ARC:
            self.tool_label.setText('Инструмент: Дуга')
        elif self.current_tool == Tool.SELECT:
            self.tool_label.setText('Инструмент: Выбор')
        print(self.current_tool)

    def update_cone_count(self):
        self.cone_label.setText(
            f'Конусов: {len(self.track.cones)}'
            )
    
    def create_cone(self, x, y):
        cone = Cone(x, y)
        self.track.add_cone(cone)
        self.update_cone_count()
        
    def on_canvas_click(self, x, y):
        
        if self.current_tool == Tool.SELECT:
            cone = self.track.get_cone_at(x, y)
            self.select_cone(cone)
            print(self.selected_cone)
        elif self.current_tool == Tool.CONE:
            self.create_cone(x, y)
            
        else:
            print('another')
            
        self.canvas.update() 

    def select_cone(self, cone):
        if self.selected_cone:
            self.selected_cone.selected= False
        if cone:
            cone.selected = True
        self.selected_cone = cone

        

    def create_canvas(self):
        self.canvas = Canvas(self.track, self.update_coordinates, self.on_canvas_click, self)
        self.setCentralWidget(self.canvas)

    def create_status_bar(self):
        self.statusbar = self.statusBar()
        self.x_label = QLabel(f'x: {0}', self)
        self.y_label = QLabel(f'y: {0}', self)
        self.zoom_label = QLabel(f'Масштаб: {zoom}%', self)
        self.cone_label = QLabel(f'Конусов: 0', self)
        self.tool_label = QLabel('Инструмент: Выбор ', self)
        self.statusbar.addPermanentWidget(self.x_label)
        self.statusbar.addPermanentWidget(self.y_label)
        self.statusbar.addPermanentWidget(self.zoom_label)
        self.statusbar.addPermanentWidget(self.cone_label)
        self.statusbar.addPermanentWidget(self.tool_label)