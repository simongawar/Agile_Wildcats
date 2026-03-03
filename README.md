# Product Development Management System (PDMS) Guide (Readme.md)

Authors: Simon G.Dak ,Osvaldo Estrell, Tousar Mohammed, Wesley Nguyen

Date: 2026-25-02  

This guide (Readme.md) provide developer onboarding explains about the project ,  setup, usage, and testing so contributors can get started quickly. Inline comments highlight customizable sections.

## About PDMS

The Product Development Management System is an Agile project management tool that allows users to manage Product Backlog.

This system allows team members to add new tasks to the Product Backlog, set and change priority for a task, move a task from the Product Backlog to the current Sprint Backlog, and then move a task from the Sprint Backlog to the Ready for Test status.


Once tested, the task is either failed and sent back for re-work in a Sprint or passed and marked as complete and ready for release.

---

## Project Setup

## 1. Clone the repository

```bash
git clone https://github.com/tousarM/Agile_Wildcats.git
cd pdms
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows:

  ```bash
  venv\Scripts\activate
  ```

- macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the server

```bash
python manage.py runserver
```

---

## Routes (with `/pdms/` prefix)

- Home → `http://127.0.0.1:8000/pdms/`  
- About → `http://127.0.0.1:8000/pdms/about/`  
- Downloads → `http://127.0.0.1:8000/pdms/downloads/`  
- Dashboard → `http://127.0.0.1:8000/pdms/dashboard/<user_id>/`  
- Task detail → `http://127.0.0.1:8000/pdms/task/<task_id>/`  
- API upload CSV → `http://127.0.0.1:8000/pdms/api/upload/csv/`  
- Admin panel → `http://127.0.0.1:8000/admin/`  

 If you try `/about/` directly, you’ll get a 404 because all app routes are prefixed with `/pdms/`.

---

```
project_root/
│   manage.py
│   requirements.txt
│   Dockerfile
│   docker-compose.yml
│   README.md
│   .gitignore
│
├── PDMS/                # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pdms_app/            # Main app
│   ├── models.py        # UserProfile, Team, Task, TaskFile
│   ├── views.py         # Dashboard, file upload, exports
│   ├── urls.py          # App routes
│   └── templates/
│       └── pdms_app/
│           ├── home.html
│           ├── about.html
│           ├── download.html
│           ├── dashboard.html
│           └── task_detail.html
└── templates/
    └── base.html        # Global layout
```

---

## Usage Guide

### User Profiles

- Each user has a profile with Name, Email, Role, Contact Info.
- Users can belong to multiple teams.
- Dashboard shows assigned tasks and team memberships.

### Tasks

- Tasks can be assigned to users.
- Each task supports file attachments (upload/download).
- Tasks can be exported to CSV, PDF, DOCX.

### File Uploads

- Files are stored in `MEDIA_ROOT/task_files/`.
- Other users can download attached files from the task detail page.

---

## Acceptance Testing

- File Upload/Download:  
  - Create a task in admin.  
  - Visit `/pdms/task/<task_id>/`.  
  - Upload a file → appears under “Attached Files.”  
  - Other users can download via link.  

- User Profile Dashboard:  
  - Create users with different roles and teams.  
  - Assign tasks.  
  - Visit `/pdms/dashboard/<user_id>/` → Profile shows correct details.  

---

## 🛠 Development Notes

- Use `{% url %}` in templates for dynamic routing (avoid hardcoding paths).
- Keep `requirements.txt` updated with `pip freeze > requirements.txt`.
- Add new models/views with comments for clarity.
- Run tests before pushing changes.

---

##  Next Steps

- Implement Team Dashboard (show all members + tasks).
- Add search/filter for tasks and users.
- Extend API endpoints for frontend integration.
