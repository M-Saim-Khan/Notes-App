from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #automatically fill 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes") #one to many rel, one user have many notes, when user delete,
    #delete all notes related name means let user have access to notes using .notes as we put "notes" which will let them access all their notes
    def __str__(self):
        return self.title