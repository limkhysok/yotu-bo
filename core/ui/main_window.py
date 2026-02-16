from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
    QStackedWidget,
)
from PyQt6.QtCore import Qt
from core.ui.layout.navbar import Navbar
from core.ui.theme import STYLESHEET


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YotuBo | Professional YouTube Automation")
        self.setMinimumSize(1100, 800)
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

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        side_layout = QVBoxLayout(self.sidebar)
        side_layout.setContentsMargins(0, 30, 0, 0)
        side_layout.setSpacing(5)

        self.menu_btns = []
        menu_items = [("📊 Overview", 0), ("🚀 Project", 1), ("⚙️ Settings", 2)]

        for text, idx in menu_items:
            btn = QPushButton(text)
            btn.setObjectName("sidebar-item")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, i=idx: self.switch_page(i))
            side_layout.addWidget(btn)
            self.menu_btns.append(btn)

        side_layout.addStretch()
        body_layout.addWidget(self.sidebar)

        # Content Stack
        self.stack = QStackedWidget()
        body_layout.addWidget(self.stack)

        main_layout.addLayout(body_layout)

    def add_page(self, widget):
        self.stack.addWidget(widget)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.menu_btns):
            btn.setProperty("active", "true" if i == index else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)
