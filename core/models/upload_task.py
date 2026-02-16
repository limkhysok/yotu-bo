from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    PENDING = "Pending"
    UPLOADING = "Uploading"
    COMPLETED = "Completed"
    FAILED = "Failed"


@dataclass
class UploadTask:
    video_path: str
    video_name: str
    status: TaskStatus = TaskStatus.PENDING
    error_message: str = ""
