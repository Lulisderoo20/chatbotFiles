# chatbotFiles

Lab repository for chatbot experiments in Python.

This repository is intentionally organized as an experiments sandbox, not as a single product.
When one experiment becomes stable, it should graduate to its own product repository.

## What this repo is

- A place to test ideas quickly.
- A shared space for related chatbot prototypes.
- A learning/validation environment before production.

## Experiment index

| ID | Experiment | Stack | Status |
|---|---|---|---|
| 1 | Socket chat server/client | Python sockets | runnable |
| 2 | HTTP API basic chatbot | Python `http.server` | runnable |
| 3 | Django chatbot prototype | Django + SQLite | runnable |
| 4 | Python script runner GUI | Tkinter | runnable |

## Quick start

```powershell
cd c:\Users\Usuario\Documents\reposgithub\chatbotFiles
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Interface for experiments

Use the hub menu:

```powershell
python experiment_hub.py
```

## Manual run commands

### Socket chat

Terminal 1:

```powershell
python experiments/socket_chat/chat_server.py
```

Terminal 2:

```powershell
python experiments/socket_chat/chat_client.py
```

### HTTP API basic chatbot

```powershell
python experiments/http_api/simple_api_server.py
```

Quick tests:

```powershell
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/users
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"message":"hola"}'
```

### Django chatbot prototype

```powershell
cd experiments/django_chat
python manage.py migrate
python manage.py runserver
```

Endpoints:

- `POST /chatbot/chat/`
- `GET /chatbot/history/`

### Script runner GUI

```powershell
python experiments/script_runner/ejecutor.py
```

## Repository structure

```text
chatbotFiles/
  experiment_hub.py
  experiments/
    socket_chat/
    http_api/
    django_chat/
    script_runner/
```

## Graduation rule

Move an experiment to a dedicated product repository when it has:

1. Stable objective and scope.
2. Defined API/UI contract.
3. Tests and CI.
4. Deployment strategy.
