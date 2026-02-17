from PyQt6.QtCore import QThread, pyqtSignal, QObject
from core.models.settings import AppSettings
from core.services.uploader import UploaderService


class AutomationManager(QObject):
    log_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.worker = None

    def start_automation(self, settings: AppSettings):
        if self.is_running():
            return

        self.log_signal.emit("🚀 Initializing Automation Engine...")

        # --- Thread Setup ---
        self.thread = QThread()
        self.worker = UploaderService(settings)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.status_signal.connect(self.log_signal.emit)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.error_signal.connect(self.on_error)

        self.worker.finished_signal.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def stop_automation(self):
        if self.worker:
            self.worker.stop()
            self.log_signal.emit("🛑 Sending stop signal to agent...")

    def is_running(self):
        return self.thread and self.thread.isRunning()

    def on_finished(self):
        self.cleanup()
        self.finished_signal.emit()

    def on_error(self, msg):
        self.cleanup()
        self.error_signal.emit(msg)

    def cleanup(self):
        self.thread = None
        self.worker = None
