from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QFileDialog,
)
from PyQt6.QtCore import Qt


class ProjectTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        header = QLabel("Automation Project")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(header)

        # Chrome Path
        self.chrome_path = self.create_input("Chrome User Data Path:", True)
        layout.addLayout(self.chrome_path[0])

        # Profile
        self.profile_name = self.create_input("Profile Name:", False)
        layout.addLayout(self.profile_name[0])

        # Video Dir
        self.video_dir = self.create_input("Video Directory:", True)
        layout.addLayout(self.video_dir[0])

        # Start Button
        self.start_btn = QPushButton("START AUTOMATION")
        self.start_btn.setMinimumHeight(50)
        self.start_btn.setStyleSheet("""
            QPushButton { background: #3EA6FF; color: #0F0F0F; font-weight: bold; border-radius: 8px; }
            QPushButton:hover { background: #65B8FF; }
        """)
        layout.addWidget(self.start_btn)

        # Logs
        layout.addWidget(QLabel("Console Output:"))
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        self.log_area.setStyleSheet(
            "background: #000; color: #00FF41; font-family: Consolas;"
        )
        layout.addWidget(self.log_area)

    def create_input(self, label_text, is_dir):
        container = QVBoxLayout()
        container.setSpacing(5)
        label = QLabel(label_text)
        label.setStyleSheet("color: #AAA; font-size: 13px;")
        container.addWidget(label)

        h_layout = QHBoxLayout()
        edit = QLineEdit()
        edit.setStyleSheet(
            "background: #1E1E1E; border: 1px solid #333; padding: 10px; border-radius: 5px;"
        )
        h_layout.addWidget(edit)

        if is_dir:
            btn = QPushButton("Browse")
            btn.setStyleSheet("background: #333; padding: 8px 15px;")
            btn.clicked.connect(lambda: self.browse(edit))
            h_layout.addWidget(btn)

        container.addLayout(h_layout)
        return container, edit

    def browse(self, edit):
        path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if path:
            edit.setText(path)

    def log(self, message):
        self.log_area.append(message)
        self.log_area.verticalScrollBar().setValue(
            self.log_area.verticalScrollBar().maximum()
        )
