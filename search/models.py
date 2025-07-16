import uuid
from django.db import models
from common.models import TimeStampedModel


class VideoFile(TimeStampedModel):
    video_file_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    chunks = models.JSONField()

    def __str__(self):
        return self.video_file_id