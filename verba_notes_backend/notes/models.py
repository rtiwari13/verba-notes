from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class FileAttachment(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="attachments/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.note.title}"
