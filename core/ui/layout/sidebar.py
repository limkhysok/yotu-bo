from PyQt6.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal


class Sidebar(QFrame):
    page_changed = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.menu_btns = []
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(1)

        menu_items = [("Overview", 0), ("Project", 1), ("Settings", 2)]

        for text, idx in menu_items:
            btn = QPushButton(text)
            btn.setObjectName("sidebar-item")
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet("font-size: 14px; font-weight: bold; color: #E0E0E0;")
            btn.clicked.connect(lambda checked, i=idx: self.on_btn_clicked(i))
            layout.addWidget(btn)
            self.menu_btns.append(btn)

        layout.addStretch()

    def on_btn_clicked(self, index):
        self.page_changed.emit(index)
        self.set_active_button(index)

    def set_active_button(self, index):
        for i, btn in enumerate(self.menu_btns):
            is_active = "true" if i == index else "false"
            btn.setProperty("active", is_active)
            btn.style().unpolish(btn)
            btn.style().polish(btn)
