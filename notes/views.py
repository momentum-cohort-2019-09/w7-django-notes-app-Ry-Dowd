from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import NoteForm

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
  
def notes_create(request):
  if request.method == "POST":
    form = NoteForm(request.POST)
    if form.is_valid():
      note = form.save()
      return redirect(to='all_notes')
  
  else:
    form = NoteForm()
    
    return render(request,'notes/notes_form.html', {'form':form})