from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from notes.models import Note, Comment
from notes.forms import NoteForm
from rest_framework import viewsets
from notes.serializers import UserSerializer, GroupSerializer, NoteSerializer, CommentSerializer

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
    
    
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  
class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  
class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all().order_by('created')
  serializer_class = NoteSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all().order_by('note')
  serializer_class = CommentSerializer
  
