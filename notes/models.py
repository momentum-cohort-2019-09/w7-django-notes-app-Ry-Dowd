from django.db import models

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField(help_text="This is a note")
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
        
class Comment(models.Model):
  content = models.CharField(max_length=255)
  note = models.ForeignKey(to=Note, on_delete=models.CASCADE, related_name='comments')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.content