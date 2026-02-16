from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QStackedWidget,
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YotuBo | Vision Agent")
        self.setMinimumSize(1000, 700)
        self.setup_ui()

    def setup_ui(self):
        # Apply Global Styles (moved from main.py)
        self.setStyleSheet("""
            QMainWindow { background-color: #0F0F0F; }
            QWidget { color: #F1F1F1; font-family: 'Inter', sans-serif; }
            #navbar { background-color: #1A1A1A; border-bottom: 1px solid #333; min-height: 60px; }
            #sidebar { background-color: #121212; border-right: 1px solid #333; min-width: 200px; }
            QPushButton#sidebar-item { 
                text-align: left; padding: 15px 25px; background: transparent; 
                color: #AAA; border: none; font-size: 15px;
            }
            QPushButton#sidebar-item:hover { background: #2A2A2A; color: #FFF; }
            QPushButton#sidebar-item[active="true"] { 
                background: #2A2A2A; color: #3EA6FF; border-left: 3px solid #3EA6FF; 
            }
        """)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 1. Navbar
        navbar = QFrame()
        navbar.setObjectName("navbar")
        nav_layout = QHBoxLayout(navbar)
        logo = QLabel("🎬 YotuBo")
        logo.setStyleSheet(
            "font-size: 20px; font-weight: 800; color: #FFF; margin-left: 15px;"
        )
        nav_layout.addWidget(logo)
        nav_layout.addStretch()

        gh_btn = QPushButton("GitHub")
        gh_btn.setStyleSheet(
            "background: transparent; border: 1px solid #333; padding: 5px 15px; border-radius: 5px;"
        )
        nav_layout.addWidget(gh_btn)

        user_info = QLabel("👤 John Doe")
        user_info.setStyleSheet("margin-right: 15px; margin-left: 15px;")
        nav_layout.addWidget(user_info)
        layout.addWidget(navbar)

        # 2. Main Body
        body = QHBoxLayout()
        body.setSpacing(0)

        # Sidebar
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        side_layout = QVBoxLayout(self.sidebar)
        side_layout.setContentsMargins(0, 20, 0, 0)

        self.menu_btns = []
        for i, text in enumerate(["Overview", "Project", "User"]):
            btn = QPushButton(text)
            btn.setObjectName("sidebar-item")
            btn.clicked.connect(lambda checked, idx=i: self.switch_page(idx))
            side_layout.addWidget(btn)
            self.menu_btns.append(btn)

        side_layout.addStretch()
        body.addWidget(self.sidebar)

        # Content
        self.stack = QStackedWidget()
        body.addWidget(self.stack)
        layout.addLayout(body)

    def add_page(self, widget):
        self.stack.addWidget(widget)

    def switch_page(self, index):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.menu_btns):
            btn.setProperty("active", "true" if i == index else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)
