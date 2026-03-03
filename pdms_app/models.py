# pdms_app/models.py
from django.db import models
from django.contrib.auth.models import User

# -------------------------------
# TEAM MODEL
# Author: Simon Gawar Dak
# Date: 2026-25-02
# -------------------------------
# Represents a group of users working together.
# Each team can have multiple members (linked via UserProfile).
class Team(models.Model):
    name = models.CharField(max_length=100)  # Team name (e.g., "Backend Team")
    description = models.TextField(blank=True)  # Optional description of the team

    def __str__(self):
        return self.name


# -------------------------------
# USER PROFILE MODEL
# -------------------------------
# Extends Django's built-in User model with additional fields.
# Each user has one profile that stores role, contact info, and team memberships.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    # Link to Django's built-in User (username, password, email, etc.)
    role = models.CharField(max_length=100)  
    # Role in the system (e.g., "Developer", "Manager")
    contact_number = models.CharField(max_length=20, blank=True)  
    # Optional phone number or other contact info
    teams = models.ManyToManyField(Team, related_name="members")  
    # User can belong to multiple teams

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# -------------------------------
# TASK MODEL
# -------------------------------
# Represents a work item assigned to a user.
# Each task has a title, description, and an optional assigned user.
class Task(models.Model):
    title = models.CharField(max_length=200)  # Short title of the task
    description = models.TextField()  # Detailed description of the task
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )  
    # Link to the user assigned to this task. If user is deleted, task remains but assigned_to becomes NULL.

    def __str__(self):
        return self.title


# -------------------------------
# TASK FILE MODEL
# -------------------------------
# Represents files attached to tasks.
# Each file belongs to a specific task and is stored in MEDIA_ROOT/task_files/.
class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="files")  
    # Link file to a specific task. If task is deleted, files are deleted too.
    file = models.FileField(upload_to="task_files/")  
    # File upload location (MEDIA_ROOT/task_files/)
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    # Timestamp when file was uploaded

    def __str__(self):
        return f"{self.task.title} - {self.file.name}"
