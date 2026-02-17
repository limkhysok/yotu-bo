from dataclasses import dataclass, field

from datetime import datetime


@dataclass
class Task:
    task_name: str = ""
    chrome_path: str = ""
    youtube_url: str = ""
    video_directory: str = ""
    post_video: int = 1
    id: int = 0
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    status: str = "Idle"

    def to_dict(self):
        return {
            "id": self.id,
            "task_name": self.task_name,
            "chrome_path": self.chrome_path,
            "youtube_url": self.youtube_url,
            "video_directory": self.video_directory,
            "post_video": self.post_video,
            "created_at": self.created_at,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
