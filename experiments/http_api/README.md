# HTTP API Experiment

Run server:

```powershell
python experiments/http_api/simple_api_server.py
```

Test endpoints:

```powershell
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/users
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"message":"hola"}'
```
