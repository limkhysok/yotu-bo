import os
import subprocess


def kill_chrome():
    """Forces all Chrome instances to close."""
    try:
        os.system("taskkill /f /im chrome.exe")
        return True
    except Exception:
        return False


def get_video_files(directory):
    """Returns a list of .mp4 files in the directory."""
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith(".mp4")]
