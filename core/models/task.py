from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class Task:
    name: str
    chrome_path: str
    video_dir: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    profile_name: str = "Default"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    status: str = "Idle"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "chrome_path": self.chrome_path,
            "video_dir": self.video_dir,
            "profile_name": self.profile_name,
            "created_at": self.created_at,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
