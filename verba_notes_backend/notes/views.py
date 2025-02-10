from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Note, FileAttachment
from .serializers import NoteSerializer, FileAttachmentSerializer

# List & Create Notes
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update & Delete a Note
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

# Upload File Attachment
class FileAttachmentUploadView(generics.CreateAPIView):
    serializer_class = FileAttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        note_id = self.kwargs.get("note_id")
        note = Note.objects.filter(id=note_id, owner=request.user).first()

        if not note:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(note=note)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
