# pdms_app/admin.py
from django.contrib import admin
from .models import Task, TaskFile, UserProfile, Team   #  Removed UploadedCSV

# Register Task model in admin
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'assigned_to')
    search_fields = ('title', 'description')
    list_filter = ('assigned_to',)

# Register TaskFile model in admin
@admin.register(TaskFile)
class TaskFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'file', 'uploaded_at')
    search_fields = ('task__title',)
    list_filter = ('uploaded_at',)

# Register UserProfile model in admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role', 'contact_number')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)

# Register Team model in admin
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
