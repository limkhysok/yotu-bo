from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont, QDesktopServices
from core.ui.views.custom_icons import CustomIcon
from core.ui.theme import THEME_COLORS


class Navbar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("navbar")
        self.setup_ui()

    def setup_ui(self):
        # Styles moved to theme.py
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(15)

        # --- Left Side: Logo & Brand ---
        logo_container = QHBoxLayout()
        self.logo_icon = QLabel("🎬")
        self.logo_icon.setFont(QFont("Segoe UI Emoji", 24))

        self.logo_text = QLabel("YotuBo")
        self.logo_text.setObjectName("logo-text")
        self.logo_text.setStyleSheet(
            f"font-size: 22px; font-weight: 800; color: {THEME_COLORS['SILVER_TEXT']}; margin-left:10px;"
        )

        logo_container.addWidget(self.logo_icon)
        logo_container.addWidget(self.logo_text)
        layout.addLayout(logo_container)

        layout.addStretch()

        # --- Right Side: Social Icons ---
        self.github_btn = QPushButton()
        self.github_btn.setObjectName("nav-action-btn")
        self.github_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.github_btn.setToolTip("GitHub Repository")

        gh_layout = QHBoxLayout(self.github_btn)
        gh_layout.setContentsMargins(0, 0, 0, 0)
        self.gh_icon = CustomIcon("github", THEME_COLORS["SILVER_TEXT"])
        gh_layout.addWidget(self.gh_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        self.github_btn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://github.com/your-repo"))
        )

        self.telegram_btn = QPushButton()
        self.telegram_btn.setObjectName("nav-action-btn")
        self.telegram_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.telegram_btn.setToolTip("Telegram Channel")

        tg_layout = QHBoxLayout(self.telegram_btn)
        tg_layout.setContentsMargins(0, 0, 0, 0)
        self.tg_icon = CustomIcon("telegram", THEME_COLORS["SILVER_TEXT"])
        tg_layout.addWidget(self.tg_icon, alignment=Qt.AlignmentFlag.AlignCenter)
        self.telegram_btn.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl("https://t.me/your-channel"))
        )

        layout.addWidget(self.github_btn)
        layout.addWidget(self.telegram_btn)
