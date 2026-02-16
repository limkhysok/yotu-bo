from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame


class OverviewPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        header = QLabel("Dashboard Overview")
        header.setStyleSheet("font-size: 28px; font-weight: bold; color: #FFFFFF;")
        layout.addWidget(header)

        # Statistics Cards
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)

        stats = [
            ("Total Videos", "42", "#3EA6FF"),
            ("Hours Saved", "12.5", "#03DAC6"),
            ("Success Rate", "98%", "#BB86FC"),
        ]

        for label, value, color in stats:
            card = self.create_stat_card(label, value, color)
            stats_layout.addWidget(card)

        layout.addLayout(stats_layout)

        # Activity Feed Placeholder
        activity_section = QFrame()
        activity_section.setStyleSheet("""
            QFrame {
                background-color: #1A1A1A;
                border: 1px solid #333;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        activity_layout = QVBoxLayout(activity_section)

        feed_header = QLabel("Recent Activity")
        feed_header.setStyleSheet(
            "font-size: 18px; font-weight: 600; color: #FFFFFF; margin-bottom: 10px;"
        )
        activity_layout.addWidget(feed_header)

        # Add a few mockup items
        for item in [
            "Video 'Unboxing.mp4' uploaded",
            "Automation started",
            "Settings updated",
        ]:
            feed_item = QLabel(f"• {item}")
            feed_item.setStyleSheet("color: #AAAAAA; font-size: 14px; padding: 5px 0;")
            activity_layout.addWidget(feed_item)

        layout.addWidget(activity_section)
        layout.addStretch()

    def create_stat_card(self, label, value, color):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #1A1A1A;
                border: 1px solid #333;
                border-radius: 12px;
                padding: 25px;
            }
        """)
        vbox = QVBoxLayout(card)
        vbox.setSpacing(10)

        lbl = QLabel(label)
        lbl.setStyleSheet("color: #AAAAAA; font-size: 14px; font-weight: 600;")

        val = QLabel(value)
        val.setStyleSheet(f"color: {color}; font-size: 32px; font-weight: 800;")

        vbox.addWidget(lbl)
        vbox.addWidget(val)
        return card
