import os

from celery import Celery


# Define settings do Django para o processo do Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


app = Celery("core")

# Lê configurações do Django prefixadas com CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descobre tasks automaticamente em apps instalados
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    return f"Request: {self.request!r}"