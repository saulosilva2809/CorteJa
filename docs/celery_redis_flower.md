# Celery, Redis e Flower

Este guia explica como executar Celery (worker e beat), Redis (broker/result) e Flower (monitoramento) no projeto CorteJá.

## Pré-requisitos

- Python virtualenv ativo
- Redis rodando localmente
  - Opção Docker (recomendado no Windows):
    - `docker run -d --name redis -p 6379:6379 redis:7-alpine`
  - Alternativas: Memurai (Windows), WSL2 com Redis.

## Variáveis de ambiente

Crie um arquivo `.env` dentro de `src/` baseado no `src/.env.example`:

```
SECRET_KEY=defina_um_seguro
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/1
```

## Executar Celery (Windows)

No Windows use `--pool=solo` para o worker.

1) Worker (em `c:\Users\saulo\python-projects\CorteJa\src`):

```
celery -A core worker -l info --pool=solo
```

2) Beat (agendador):

```
celery -A core beat -l info
```

3) Flower (dashboard):

PowerShell (usa variável de ambiente carregada do `.env`):

```
flower -A core --port=5555 --broker $env:CELERY_BROKER_URL
```

Abra: http://localhost:5555/

## Testar tarefa

Há uma tarefa exemplo em `apps.base.tasks.ping_task`. Com Redis e worker rodando:

```
python -c "from apps.base.tasks import ping_task; r = ping_task.delay('Saulo'); print('Task ID:', r.id)"
```

No Flower você deve ver a execução; no terminal do worker, o processamento.

## Estrutura adicionada

- `core/celery.py`: configuração do app Celery
- `core/__init__.py`: integração para autodiscovery
- `apps/base/tasks.py`: tarefa exemplo
- `core/settings.py`: variáveis `CELERY_*`
- `src/.env.example`: variáveis de ambiente

## Dicas

- Se o worker não conecta, verifique se o Redis está acessível em `localhost:6379`.
- Para produção, considere URLs protegidas e instâncias gerenciadas de Redis.