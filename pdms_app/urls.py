# pdms_app/urls.py

# Author: Simon Gawar Dak
# Date: 2026-25-02

from django.urls import path
from . import views   # Import all view functions from views.py

# URL patterns define how requests are routed to views
urlpatterns = [
    # Home page route
    path("", views.home, name="home"),

    # About page route
    path("about/", views.about_page, name="about"),

    # Downloads page route (export + upload functionality)
    path("downloads/", views.download_page, name="download_page"),

    # Task detail page (shows task info + attached files)
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),

    # File upload route for a specific task
    path("task/<int:task_id>/upload/", views.upload_task_file, name="upload_task_file"),

    # User dashboard route (shows profile, teams, assigned tasks)
    path("dashboard/<int:user_id>/", views.user_dashboard, name="user_dashboard"),

    # API endpoints for CSV/PDF/DOCX export and CSV upload
    path("api/upload/csv/", views.upload_csv, name="upload_csv"),
    path("api/export/csv/", views.export_csv, name="export_csv"),
    path("api/export/pdf/", views.export_pdf, name="export_pdf"),
    path("api/export/docx/", views.export_docx, name="export_docx"),
]
