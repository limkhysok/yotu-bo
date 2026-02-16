import pyautogui
import time
import random


def wait_and_click(image_path, confidence=0.8, timeout=30):
    """Searches for an image on screen and clicks it when found."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if location:
                pyautogui.click(location)
                # Random human-like delay
                time.sleep(random.uniform(1.5, 3.5))
                return True
        except Exception:
            pass
        time.sleep(1)
    return False


def check_exists(image_path, confidence=0.8):
    """Checks if an image exists on screen without clicking."""
    try:
        return pyautogui.locateOnScreen(image_path, confidence=confidence) is not None
    except Exception:
        return False
