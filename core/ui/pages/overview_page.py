from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from core.ui.theme import THEME_COLORS


class OverviewPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        header = QLabel("Dashboard Overview")
        header.setObjectName("page-header")
        layout.addWidget(header)

        # Statistics Cards
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)

        stats = [
            ("Total Videos", "42", THEME_COLORS["PRIMARY_RED"]),
            ("Hours Saved", "12.5", THEME_COLORS["SILVER_METALLIC"]),
            ("Success Rate", "98%", THEME_COLORS["SILVER_METALLIC"]),
        ]

        for label, value, color in stats:
            card = self.create_stat_card(label, value, color)
            stats_layout.addWidget(card)

        layout.addLayout(stats_layout)

        # Activity Feed Placeholder
        activity_section = QFrame()
        activity_section.setObjectName("card")
        activity_layout = QVBoxLayout(activity_section)

        feed_header = QLabel("Recent Activity")
        feed_header.setStyleSheet(
            f"font-size: 18px; font-weight: 600; color: {THEME_COLORS['PRIMARY_RED']}; margin-bottom: 10px;"
        )
        activity_layout.addWidget(feed_header)

        # Add a few mockup items
        for item in [
            "Video 'Unboxing.mp4' uploaded",
            "Automation started",
            "Settings updated",
        ]:
            feed_item = QLabel(f"• {item}")
            feed_item.setStyleSheet(
                f"color: {THEME_COLORS['SILVER_TEXT']}; font-size: 14px; padding: 5px 0;"
            )
            activity_layout.addWidget(feed_item)

        layout.addWidget(activity_section)
        layout.addStretch()

    def create_stat_card(self, label, value, color):
        card = QFrame()
        card.setObjectName("card")
        vbox = QVBoxLayout(card)
        vbox.setSpacing(10)

        lbl = QLabel(label)
        lbl.setStyleSheet(
            f"color: {THEME_COLORS['SILVER_METALLIC']}; font-size: 14px; font-weight: 600;"
        )

        val = QLabel(value)
        val.setStyleSheet(f"color: {color}; font-size: 32px; font-weight: 800;")

        vbox.addWidget(lbl)
        vbox.addWidget(val)
        return card
