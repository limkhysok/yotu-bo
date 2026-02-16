from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt
from core.ui.theme import THEME_COLORS


class TaskPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(10)

        # Header Section
        header_container = QHBoxLayout()

        header = QLabel("Tasks")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #D32F2F;")
        header.setObjectName("page-header")

        self.create_btn = QPushButton("Create")
        self.create_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.create_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {THEME_COLORS["PRIMARY_RED"]};
                color: {THEME_COLORS["SILVER_TEXT"]};
                padding: 6px 20px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background-color: {THEME_COLORS["DARK_RED"]};
            }}
        """)

        header_container.addWidget(header)
        header_container.addStretch()
        header_container.addWidget(self.create_btn)

        layout.addLayout(header_container)
        layout.addStretch()

    def log(self, message):
        print(f"[LOG]: {message}")
