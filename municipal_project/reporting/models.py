from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = [
    ('Submitted', 'Submitted'),
    ('Assigned', 'Assigned'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Reopened', 'Reopened'),
]

class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    issue_type = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    is_draft = models.BooleanField(default=False)
    photos = models.JSONField(default=list, blank=True)  # Store photo URLs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.issue_type} - {self.location}"

class StatusUpdate(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='updates')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

class Message(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']