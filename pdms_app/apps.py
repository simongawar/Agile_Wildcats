from django.apps import AppConfig

class PdmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdms_app'   # <-- must match folder name
