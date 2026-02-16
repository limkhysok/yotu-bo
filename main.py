import sys
import os

# Suppress the internal Qt DPI warning
os.environ["QT_LOGGING_RULES"] = "qt.qpa.window=false"

from PyQt6.QtWidgets import QApplication, QLabel, QMessageBox
from core.ui.main_window import MainWindow
from core.ui.project_tab import ProjectTab
from core.services.uploader import UploaderService
from core.models.settings import AppSettings
from PyQt6.QtCore import QThread


class YotuBoApp:
    def __init__(self):
        try:
            self.app = QApplication(sys.argv)
            self.window = MainWindow()

            # Initialize Tabs
            self.project_tab = ProjectTab()

            # Mock Pages for Overview and User
            overview = QLabel("Dashboard Overview (Mock)")
            overview.setStyleSheet("font-size: 30px; margin: 50px;")
            user_page = QLabel("User Profile (Mock)")
            user_page.setStyleSheet("font-size: 30px; margin: 50px;")

            # Add to stack
            self.window.add_page(overview)
            self.window.add_page(self.project_tab)
            self.window.add_page(user_page)

            # Connect Actions
            self.project_tab.start_btn.clicked.connect(self.toggle_automation)

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
        # Gather Settings
        settings = AppSettings(
            chrome_user_data_path=self.project_tab.chrome_path[1].text(),
            profile_name=self.project_tab.profile_name[1].text(),
            video_directory=self.project_tab.video_dir[1].text(),
        )

        if not settings.chrome_user_data_path or not settings.video_directory:
            from PyQt6.QtWidgets import QMessageBox

            QMessageBox.warning(self.window, "Error", "Please fill required paths.")
            return

        self.project_tab.log_area.clear()

        # Thread Setup
        self.uploader_thread = QThread()
        self.uploader_worker = UploaderService(settings)
        self.uploader_worker.moveToThread(self.uploader_thread)

        self.uploader_thread.started.connect(self.uploader_worker.run)
        self.uploader_worker.status_signal.connect(self.project_tab.log)
        self.uploader_worker.finished_signal.connect(self.on_finished)
        self.uploader_worker.error_signal.connect(self.on_error)

        self.uploader_worker.finished_signal.connect(self.uploader_thread.quit)
        self.uploader_thread.finished.connect(self.uploader_thread.deleteLater)

        self.uploader_thread.start()
        self.project_tab.start_btn.setText("STOP AUTOMATION")
        self.project_tab.start_btn.setStyleSheet("background: #CF6679; color: white;")

    def stop_automation(self):
        if self.uploader_worker:
            self.uploader_worker.stop()
            self.project_tab.log("Stopping agent...")

    def on_finished(self):
        self.reset_ui()
        QMessageBox.information(self.window, "Done", "Automation Finished!")

    def on_error(self, msg):
        self.reset_ui()
        QMessageBox.critical(self.window, "Error", msg)

    def reset_ui(self):
        self.project_tab.start_btn.setText("START AUTOMATION")
        self.project_tab.start_btn.setStyleSheet("background: #3EA6FF; color: #0F0F0F;")
        self.uploader_thread = None
        self.uploader_worker = None

    def run(self):
        self.window.switch_page(1)  # Start on Project tab
        self.window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = YotuBoApp()
    app.run()
