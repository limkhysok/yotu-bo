import os
import time
import pyautogui
import pyperclip
from PyQt6.QtCore import QObject, pyqtSignal
from core.services.browser import BrowserManager
from core.utils.vision import wait_and_click
from core.utils.system import kill_chrome, get_video_files


class UploaderService(QObject):
    status_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.is_running = True
        pyautogui.FAILSAFE = settings.fail_safe

    def log(self, message):
        self.status_signal.emit(f"[{time.strftime('%H:%M:%S')}] {message}")

    def stop(self):
        self.is_running = False

    def run(self):
        try:
            # 1. Kill Chrome
            self.log("Closing existing Chrome instances...")
            kill_chrome()
            time.sleep(2)

            # 2. Start Browser
            self.log("Launching browser...")
            browser = BrowserManager(
                self.settings.chrome_user_data_path, self.settings.profile_name
            )
            browser.start()
            browser.open_url("https://www.youtube.com")
            time.sleep(5)

            # 3. Get Tasks
            videos = get_video_files(self.settings.video_directory)
            self.log(f"Found {len(videos)} videos to upload.")

            for video_name in videos:
                if not self.is_running:
                    break

                self.log(f"Processing: {video_name}")
                video_path = os.path.abspath(
                    os.path.join(self.settings.video_directory, video_name)
                )

                # Logic sequence using vision utils
                # (Assuming images are in assets/screenshots/)
                assets_path = "assets/screenshots/"

                if not wait_and_click(
                    os.path.join(assets_path, "upload_icon.png"),
                    confidence=self.settings.confidence_level,
                ):
                    self.error_signal.emit("Upload icon not found.")
                    break

                time.sleep(2)
                pyperclip.copy(video_path)
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")

                # Metadata steps...
                wait_and_click(
                    os.path.join(assets_path, "not_made_for_kids.png"),
                    confidence=self.settings.confidence_level,
                )

                for i in range(3):
                    wait_and_click(
                        os.path.join(assets_path, "next_button.png"),
                        confidence=self.settings.confidence_level,
                    )

                wait_and_click(
                    os.path.join(assets_path, "public_radio.png"),
                    confidence=self.settings.confidence_level,
                )
                wait_and_click(
                    os.path.join(assets_path, "publish_button.png"),
                    confidence=self.settings.confidence_level,
                )

                # Wait for completion
                if wait_and_click(
                    os.path.join(assets_path, "upload_complete.png"),
                    timeout=300,
                    confidence=self.settings.confidence_level,
                ):
                    self.log(f"Successfully uploaded: {video_name}")

                pyautogui.press("esc")
                time.sleep(3)

            self.log("All tasks completed.")
            self.finished_signal.emit()

        except Exception as e:
            self.error_signal.emit(str(e))
