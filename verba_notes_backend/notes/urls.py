from django.urls import path
from .views import NoteListCreateView, NoteDetailView, FileAttachmentUploadView

urlpatterns = [
    path('', NoteListCreateView.as_view(), name='notes_list_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:note_id>/upload/', FileAttachmentUploadView.as_view(), name='file_upload'),
]
