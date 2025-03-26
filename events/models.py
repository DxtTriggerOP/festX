from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50)
    address = models.TextField(default="N/A")  # ✅ Ensures no NULL errors
    event = models.ForeignKey('Event', on_delete=models.CASCADE)  # ✅ Must be linked properly

    def __str__(self):
        return f"{self.name} - {self.event.title}"

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title