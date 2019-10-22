from django.shortcuts import render
from notes.models import Note

# Create your views here.
def notes_view(request):
  return render(request, "notes/notes_view.html", {
    "notes": Note.objects.all(),
  })
  
def notes_detail(request, pk):
  note = Note.objects.get(pk=pk)
  return render(request, "notes/notes_detail.html", {
    "note" : note
  })