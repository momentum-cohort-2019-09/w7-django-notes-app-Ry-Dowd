from django.contrib import admin

# Register your models here.
from .models import Note, Comment

class CommentInLine(admin.StackedInline):
  model=Comment
  extra=2
  
class NoteAdmin(admin.ModelAdmin):
  list_display=('title', 'updated')
  inlines=[CommentInLine]

admin.site.register(Note, NoteAdmin)
admin.site.register(Comment)