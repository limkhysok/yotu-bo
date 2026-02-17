from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QLineEdit,
    QScrollArea,
    QFileDialog,
    QGridLayout,
    QSpinBox,
)
from PyQt6.QtCore import Qt, pyqtSignal
from core.ui.theme import THEME_COLORS

from core.models.task import Task
from core.services.storage import StorageService


class TaskCard(QFrame):
    # Signals for changes to trigger storage updates
    changed = pyqtSignal()
    delete_requested = pyqtSignal()

    def __init__(self, task: Task, parent=None):
        super().__init__(parent)
        self.task = task
        self.setObjectName("card")
        self.setup_ui()
        self.load_task_data()
        self.connect_signals()

    def setup_ui(self):
        # Main layout with reduced spacing
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(8)

        # --- Header Row: Task Name & Delete ---
        header_layout = QHBoxLayout()
        self.task_name_input = QLineEdit()
        self.task_name_input.setPlaceholderText("Task Name...")
        self.task_name_input.setStyleSheet(
            "font-size: 15px; font-weight: 800; color: #D32F2F; border: none; background: transparent; padding: 0;"
        )

        self.delete_btn = QPushButton("🗑️")
        self.delete_btn.setFixedSize(24, 24)
        self.delete_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.delete_btn.setStyleSheet(
            "background: transparent; font-size: 14px; border: none; color: #666;"
        )

        header_layout.addWidget(self.task_name_input)
        header_layout.addStretch()
        header_layout.addWidget(self.delete_btn)
        layout.addLayout(header_layout)

        # --- Grid Section: Inputs ---
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.setContentsMargins(0, 0, 0, 0)

        # Row 1: YouTube URL
        self.youtube_url_input = self.create_compact_input(
            grid, 0, "YouTube URL:", "https://youtube.com/..."
        )

        # Row 2: Chrome Path
        self.chrome_path_input = self.create_compact_path_field(
            grid, 1, "Chrome Path:", "Chrome User Data..."
        )

        # Row 3: Video Directory
        self.video_directory_input = self.create_compact_path_field(
            grid, 2, "Video Directory:", "Folder with videos..."
        )

        # Row 4: Post Video Count
        self.post_video_input = self.create_compact_spinbox(
            grid, 3, "Post Video Count:", 1, 100
        )

        layout.addLayout(grid)

        # --- Footer Row: Start Button ---
        self.start_btn = QPushButton("START TASK")
        self.start_btn.setFixedHeight(34)
        self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.start_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {THEME_COLORS["PRIMARY_RED"]};
                color: {THEME_COLORS["SILVER_TEXT"]};
                border-radius: 4px;
                font-weight: 800;
                font-size: 11px;
                margin-top: 5px;
            }}
            QPushButton:hover {{
                background-color: {THEME_COLORS["DARK_RED"]};
            }}
        """)
        layout.addWidget(self.start_btn)

    def load_task_data(self):
        """Set UI values from the Task object."""
        self.task_name_input.setText(self.task.task_name)
        self.youtube_url_input.setText(self.task.youtube_url)
        self.chrome_path_input.setText(self.task.chrome_path)
        self.video_directory_input.setText(self.task.video_directory)
        self.post_video_input.setValue(self.task.post_video)

    def connect_signals(self):
        """Connect UI changes to the 'changed' signal."""
        self.task_name_input.textChanged.connect(self.on_data_changed)
        self.youtube_url_input.textChanged.connect(self.on_data_changed)
        self.chrome_path_input.textChanged.connect(self.on_data_changed)
        self.video_directory_input.textChanged.connect(self.on_data_changed)
        self.post_video_input.valueChanged.connect(self.on_data_changed)
        self.delete_btn.clicked.connect(self.delete_requested.emit)

    def on_data_changed(self):
        """Update the internal Task object and notify the page."""
        self.task.task_name = self.task_name_input.text()
        self.task.youtube_url = self.youtube_url_input.text()
        self.task.chrome_path = self.chrome_path_input.text()
        self.task.video_directory = self.video_directory_input.text()
        self.task.post_video = self.post_video_input.value()
        self.changed.emit()

    def create_compact_input(self, grid, row, label_text, placeholder):
        lbl = QLabel(label_text)
        lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-size: 11px; font-weight: 600;"
        )
        grid.addWidget(lbl, row, 0)

        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedHeight(28)
        input_field.setStyleSheet("font-size: 12px; padding: 4px 8px;")
        grid.addWidget(input_field, row, 1, 1, 2)
        return input_field

    def create_compact_path_field(self, grid, row, label_text, placeholder):
        lbl = QLabel(label_text)
        lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-size: 11px; font-weight: 600;"
        )
        grid.addWidget(lbl, row, 0)

        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedHeight(28)
        input_field.setStyleSheet("font-size: 12px; padding: 4px 8px;")

        browse_btn = QPushButton("Browse")
        browse_btn.setFixedSize(60, 28)
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #1A1A1A;
                border: 1px solid #333;
                border-radius: 3px;
                color: #AAA;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #222;
                color: #EEE;
            }
        """)
        browse_btn.clicked.connect(lambda: self.on_browse(input_field))

        grid.addWidget(input_field, row, 1)
        grid.addWidget(browse_btn, row, 2)
        return input_field

    def create_compact_spinbox(self, grid, row, label_text, min_val, max_val):
        lbl = QLabel(label_text)
        lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-size: 11px; font-weight: 600;"
        )
        grid.addWidget(lbl, row, 0)

        spin = QSpinBox()
        spin.setRange(min_val, max_val)
        spin.setFixedHeight(28)
        spin.setStyleSheet("""
            QSpinBox {
                background-color: #121212;
                border: 1px solid #4A4A4A;
                border-radius: 4px;
                color: #E0E0E0;
                padding: 4px 8px;
                font-size: 12px;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                background: #1A1A1A;
                border: 1px solid #333;
                width: 16px;
            }
        """)
        grid.addWidget(spin, row, 1, 1, 2)
        return spin

    def on_browse(self, target):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
            target.setText(path)
            self.changed.emit()


class TaskPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.storage = StorageService()
        self.setup_ui()
        self.load_existing_tasks()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 15, 20, 15)
        main_layout.setSpacing(10)

        # 1. Header
        header_container = QHBoxLayout()
        header = QLabel("Tasks")
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: #D32F2F;")

        self.create_btn = QPushButton("Create")
        self.create_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.create_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {THEME_COLORS["PRIMARY_RED"]};
                color: {THEME_COLORS["SILVER_TEXT"]};
                padding: 6px 15px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }}
            QPushButton:hover {{
                background-color: {THEME_COLORS["DARK_RED"]};
            }}
        """)
        self.create_btn.clicked.connect(self.on_create_clicked)

        header_container.addWidget(header)
        header_container.addStretch()
        header_container.addWidget(self.create_btn)
        main_layout.addLayout(header_container)

        # 2. Scrollable Task Area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll.setStyleSheet("background: transparent;")

        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("background: transparent;")
        self.tasks_layout = QVBoxLayout(self.scroll_content)
        self.tasks_layout.setContentsMargins(0, 0, 5, 0)
        self.tasks_layout.setSpacing(12)

        self.scroll.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll)

        self.tasks_layout.addStretch()  # Push everything up

    def load_existing_tasks(self):
        """Fetch all tasks from storage and display their cards."""
        tasks = self.storage.load_tasks()
        for t in tasks:
            self.add_task_card(t)

    def on_create_clicked(self):
        """Create a new task with a sequential ID."""
        tasks = self.storage.load_tasks()
        next_id = 1
        if tasks:
            next_id = max(t.id for t in tasks) + 1

        new_task = Task(task_name=f"Task {next_id}", id=next_id)
        self.storage.add_task(new_task)
        self.add_task_card(new_task)

    def add_task_card(self, task: Task):
        """Create and add a TaskCard widget to the layout."""
        card = TaskCard(task)
        # Add to layout before the stretch
        self.tasks_layout.insertWidget(self.tasks_layout.count() - 1, card)

        # Connect signals
        card.changed.connect(self.persist_changes)
        card.delete_requested.connect(lambda: self.remove_task_card(card))

    def persist_changes(self):
        """Get all task objects from cards and save them to storage."""
        all_tasks = []
        for i in range(self.tasks_layout.count()):
            widget = self.tasks_layout.itemAt(i).widget()
            if isinstance(widget, TaskCard):
                all_tasks.append(widget.task)
        self.storage.save_tasks(all_tasks)

    def remove_task_card(self, card):
        """Delete task from storage and remove card from UI."""
        self.storage.delete_task(card.task.id)
        self.tasks_layout.removeWidget(card)
        card.deleteLater()

    def log(self, message):
        print(f"[LOG]: {message}")
