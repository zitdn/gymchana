from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.resize(1400, 900)
        self.setMinimumSize(900, 600)
        self.setWindowTitle('Gymkhana Designer')

