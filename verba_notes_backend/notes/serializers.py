from rest_framework import serializers
from .models import Note, FileAttachment

class FileAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAttachment
        fields = ['id', 'file', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

class NoteSerializer(serializers.ModelSerializer):
    attachments = FileAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at', 'is_archived', 'is_pinned', 'attachments']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
