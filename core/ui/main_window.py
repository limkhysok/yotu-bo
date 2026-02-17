from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
)
from core.ui.layout.navbar import Navbar
from core.ui.layout.sidebar import Sidebar
from core.ui.theme import STYLESHEET


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YotuBo")
        self.resize(900, 700)
        self.setup_ui()

    def setup_ui(self):
        # Apply Centralized Stylesheet
        self.setStyleSheet(STYLESHEET)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. Navbar
        self.navbar = Navbar(self)
        main_layout.addWidget(self.navbar)

        # 2. Main Body (Sidebar + Content)
        body_layout = QHBoxLayout()
        body_layout.setSpacing(0)

        # Sidebar Component
        self.sidebar = Sidebar(self)
        self.sidebar.page_changed.connect(self.switch_page)
        body_layout.addWidget(self.sidebar)
        body_layout.setContentsMargins(0, 0, 0, 0)

        # Content Stack
        self.stack = QStackedWidget()
        body_layout.addWidget(self.stack)

        main_layout.addLayout(body_layout)

    def add_page(self, widget):
        self.stack.addWidget(widget)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        self.sidebar.set_active_button(index)
