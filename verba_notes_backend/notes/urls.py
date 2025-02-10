from django.urls import path
from .views import NoteListCreateView, NoteDetailView

urlpatterns = [
    path('', NoteListCreateView.as_view(), name='notes_list_create'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]
