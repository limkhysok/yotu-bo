import sys
import os

# Suppress internal Qt warnings (DPI and Fonts)
os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false;qt.qpa.fonts=false"

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase

# UI Imports
from core.ui.main_window import MainWindow
from core.ui.pages.overview_page import OverviewPage
from core.ui.pages.task_page import TaskPage
from core.ui.pages.settings_page import SettingsPage


class YotuBoApp:
    def __init__(self):
        try:
            self.app = QApplication(sys.argv)

            # Load Custom Font
            font_path = os.path.join("assets", "fonts", "Jost-Regular.ttf")
            if os.path.exists(font_path):
                QFontDatabase.addApplicationFont(font_path)

            self.window = MainWindow()

            # 1. Initialize Pages
            self.overview_page = OverviewPage()
            self.task_page = TaskPage()
            self.settings_page = SettingsPage()

            # 2. Add to Main Window Stack
            self.window.add_page(self.overview_page)
            self.window.add_page(self.task_page)
            self.window.add_page(self.settings_page)

        except Exception as e:
            print(f"Startup Error: {e}")
            sys.exit(1)

    def run(self):
        self.window.switch_page(0)  # Default to Overview
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = YotuBoApp()
    app.run()
