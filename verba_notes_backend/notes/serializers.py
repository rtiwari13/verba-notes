from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at', 'updated_at', 'is_archived', 'is_pinned']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']
