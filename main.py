import sys
import os

# Suppress internal Qt warnings (DPI and Fonts)
os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false;qt.qpa.fonts=false"

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QThread
from PyQt6.QtGui import QFontDatabase

# UI Imports
from core.ui.main_window import MainWindow
from core.ui.pages.overview_page import OverviewPage
from core.ui.pages.task_page import TaskPage
from core.ui.pages.settings_page import SettingsPage


from core.services.uploader import UploaderService
from core.models.settings import AppSettings


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

            # 3. Connect UI Actions
            # self.task_page.start_btn.clicked.connect(self.toggle_automation)

            # Process & Threading
            self.uploader_thread = None
            self.uploader_worker = None

        except Exception as e:
            print(f"Startup Error: {e}")
            sys.exit(1)

    def toggle_automation(self):
        if self.uploader_thread and self.uploader_thread.isRunning():
            self.stop_automation()
        else:
            self.start_automation()

    def start_automation(self):
        # Gather Settings from UI (Placeholder since widgets were removed)
        settings = AppSettings(
            chrome_user_data_path="",
            profile_name="",
            video_directory="",
            confidence_level=float(self.settings_page.conf_val.text()),
            fail_safe=self.settings_page.fail_safe_cb.isChecked(),
        )

        if not settings.chrome_user_data_path or not settings.video_directory:
            QMessageBox.warning(
                self.window,
                "Configuration Error",
                "Please provide all required directory paths in the Tasks tab.",
            )
            return

        # self.task_page.log_area.clear()
        self.task_page.log("🚀 Initializing Automation Engine...")

        # --- Thread Setup ---
        self.uploader_thread = QThread()
        self.uploader_worker = UploaderService(settings)
        self.uploader_worker.moveToThread(self.uploader_thread)

        self.uploader_thread.started.connect(self.uploader_worker.run)
        self.uploader_worker.status_signal.connect(self.task_page.log)
        self.uploader_worker.finished_signal.connect(self.on_finished)
        self.uploader_worker.error_signal.connect(self.on_error)

        self.uploader_worker.finished_signal.connect(self.uploader_thread.quit)
        self.uploader_thread.finished.connect(self.uploader_thread.deleteLater)

        self.uploader_thread.start()

        # Update Button State (Stop Style)
        # self.task_page.start_btn.setText("STOP AUTOMATION")
        # self.task_page.start_btn.setStyleSheet(
        #     f"background: {THEME_COLORS['DARK_RED']}; color: {THEME_COLORS['SILVER_TEXT']}; border-radius: 8px;"
        # )

    def task_dir_gather(self):
        # Placeholder
        return ""

    def stop_automation(self):
        if self.uploader_worker:
            self.uploader_worker.stop()
            self.task_page.log("🛑 Sending stop signal to agent...")

    def on_finished(self):
        self.reset_ui()
        QMessageBox.information(
            self.window, "Success", "All video uploads have been processed."
        )

    def on_error(self, msg):
        self.reset_ui()
        QMessageBox.critical(self.window, "Critical Automation Error", msg)

    def reset_ui(self):
        # self.task_page.start_btn.setText("START AUTOMATION")
        # self.task_page.start_btn.setStyleSheet(
        #     f"background-color: {THEME_COLORS['PRIMARY_RED']}; color: {THEME_COLORS['SILVER_TEXT']}; border-radius: 8px; font-weight: 800;"
        # )
        self.uploader_thread = None
        self.uploader_worker = None

    def run(self):
        self.window.switch_page(0)  # Default to Overview
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = YotuBoApp()
    app.run()
