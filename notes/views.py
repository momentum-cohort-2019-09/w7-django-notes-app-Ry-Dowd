from django.shortcuts import render
from notes.data import NOTES

# Create your views here.
def notes_view(request):
  return render(request, "notes/notes_view.html", {
    "notes": NOTES,
  })
  
def notes_detail(request, pk):
  note = NOTES[str(pk)]
  return render(request, "notes/notes_detail.html", {
    "note" : note
  })