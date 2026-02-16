from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
    QFrame,
)
from PyQt6.QtCore import Qt
from core.ui.theme import THEME_COLORS


class ProjectPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)

        header = QLabel("Automation Project")
        header.setObjectName("page-header")
        layout.addWidget(header)

        # Configuration Section
        config_card = QFrame()
        config_card.setObjectName("card")
        config_layout = QVBoxLayout(config_card)
        config_layout.setSpacing(20)

        self.chrome_path_input = self.create_input_field(
            config_layout,
            "Chrome User Data Path:",
            "Select your Chrome profile directory",
        )
        self.profile_name_input = self.create_input_field(
            config_layout, "Profile Name:", "e.g., Default or Profile 1", is_dir=False
        )
        self.video_dir_input = self.create_input_field(
            config_layout, "Video Directory:", "Select folder containing MP4 files"
        )

        layout.addWidget(config_card)

        # Action Button
        self.start_btn = QPushButton("START AUTOMATION")
        self.start_btn.setObjectName("primary-btn")
        self.start_btn.setMinimumHeight(55)
        self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(self.start_btn)

        # Console Output
        status_lbl = QLabel("Live Status Console:")
        status_lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-weight: 600;"
        )
        layout.addWidget(status_lbl)
        self.log_area = QTextEdit()
        self.log_area.setObjectName("console")
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

    def create_input_field(self, parent_layout, label_text, placeholder, is_dir=True):
        container = QVBoxLayout()
        container.setSpacing(8)

        lbl = QLabel(label_text)
        lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-size: 14px; font-weight: 600;"
        )
        container.addWidget(lbl)

        h_layout = QHBoxLayout()
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        h_layout.addWidget(line_edit)

        if is_dir:
            browse_btn = QPushButton("Browse")
            browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            browse_btn.setFixedWidth(100)
            browse_btn.setStyleSheet("""
                QPushButton {
                    background-color: #1E1E1E;
                    color: #E0E0E0;
                    border: 1px solid #4A4A4A;
                    border-radius: 6px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #D32F2F;
                    color: #E0E0E0;
                }
            """)
            browse_btn.clicked.connect(lambda: self.browse_folder(line_edit))
            h_layout.addWidget(browse_btn)

        container.addLayout(h_layout)
        parent_layout.addLayout(container)
        return line_edit

    def browse_folder(self, target_line_edit):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            target_line_edit.setText(folder)

    def log(self, message):
        self.log_area.append(message)
        self.log_area.verticalScrollBar().setValue(
            self.log_area.verticalScrollBar().maximum()
        )
