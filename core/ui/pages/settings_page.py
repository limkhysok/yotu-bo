from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QCheckBox,
    QSlider,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        header = QLabel("Global Settings")
        header.setStyleSheet("font-size: 28px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(header)

        # Automation Settings
        auto_section = self.create_section("Automation Logic")
        auto_layout = auto_section[1]

        self.fail_safe_cb = QCheckBox(
            "Enable PyAutoGUI Fail-Safe (Mouse to corner stops app)"
        )
        self.fail_safe_cb.setChecked(True)
        self.fail_safe_cb.setStyleSheet("color: #DDD; font-size: 14px;")

        self.human_delay_cb = QCheckBox("Simulate Human-Like Typing Delays")
        self.human_delay_cb.setChecked(True)
        self.human_delay_cb.setStyleSheet("color: #DDD; font-size: 14px;")

        auto_layout.addWidget(self.fail_safe_cb)
        auto_layout.addWidget(self.human_delay_cb)
        layout.addWidget(auto_section[0])

        # Vision Confidence
        vision_section = self.create_section("Vision Detection")
        vision_layout = vision_section[1]

        conf_label_box = QHBoxLayout()
        conf_label = QLabel("Detection Confidence Score")
        conf_label.setStyleSheet("color: #DDD; font-size: 14px;")
        self.conf_val = QLabel("0.8")
        self.conf_val.setStyleSheet("color: #3EA6FF; font-weight: bold;")
        conf_label_box.addWidget(conf_label)
        conf_label_box.addStretch()
        conf_label_box.addWidget(self.conf_val)

        self.conf_slider = QSlider(Qt.Orientation.Horizontal)
        self.conf_slider.setRange(50, 100)
        self.conf_slider.setValue(80)
        self.conf_slider.valueChanged.connect(
            lambda v: self.conf_val.setText(str(v / 100))
        )

        vision_layout.addLayout(conf_label_box)
        vision_layout.addWidget(self.conf_slider)
        layout.addWidget(vision_section[0])

        layout.addStretch()

    def create_section(self, title):
        frame = QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: #1A1A1A;
                border: 1px solid #333;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        layout = QVBoxLayout(frame)

        lbl = QLabel(title)
        lbl.setStyleSheet(
            "font-size: 18px; font-weight: 600; color: #3EA6FF; margin-bottom: 15px;"
        )
        layout.addWidget(lbl)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(15)
        layout.addLayout(content_layout)

        return frame, content_layout
