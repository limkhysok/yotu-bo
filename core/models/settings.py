from dataclasses import dataclass


@dataclass
class AppSettings:
    chrome_user_data_path: str = ""
    profile_name: str = "Default"
    video_directory: str = ""
    confidence_level: float = 0.8
    fail_safe: bool = True
