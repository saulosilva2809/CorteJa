from celery import shared_task


@shared_task
def ping_task(name: str = "mundo"):
    """Tarefa simples para testar execução do Celery."""
    return f"Olá, {name}! Celery está funcionando."