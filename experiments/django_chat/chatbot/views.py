import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import ChatMessage


def build_response(message: str) -> str:
    lower = message.lower()
    if any(word in lower for word in ["hola", "buenas", "hello"]):
        return "Hola. Soy el chatbot Django de experimento."
    if any(word in lower for word in ["precio", "comprar", "pago"]):
        return "Todavia no tengo modulo de ventas, pero puedo agregarlo."
    if any(word in lower for word in ["error", "ayuda", "soporte"]):
        return "Contame el error y lo registramos para la siguiente version."
    return "Mensaje recibido en el experimento Django."


@require_http_methods(["POST"])
def handle_message(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    message = str(payload.get("message", "")).strip()
    if not message:
        return JsonResponse({"error": "Field 'message' is required"}, status=400)

    ChatMessage.objects.create(message=message)
    response_message = build_response(message)

    return JsonResponse({"message": message, "response": response_message})


@require_http_methods(["GET"])
def history(request):
    records = ChatMessage.objects.order_by("-timestamp")[:20]
    data = [
        {
            "message": row.message,
            "timestamp": row.timestamp.isoformat(),
        }
        for row in records
    ]
    return JsonResponse({"history": data})
