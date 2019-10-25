from django.contrib.auth.models import User, Group
from rest_framework import serializers
from notes.models import Note, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
  notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
  
  class Meta:
    model = User
    fields = ['id', 'username', 'notes', 'groups']
    
class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']
    
class NoteSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Note
    fields = ['url', 'title', 'content', 'created', 'updated', 'pk', 'owner']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = ['url', 'content', 'note']
    