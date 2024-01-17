from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def handle_message(request, message):
    # Aquí puedes agregar lógica para procesar el mensaje (por ejemplo, llamando a una API de clima).
    # Guarda el mensaje en la base de datos.
    ChatMessage.objects.create(message=message)

    # Responde con un mensaje simple por ahora.
    response_message = f"Bot: Recibí tu mensaje: {message}"
    return JsonResponse({'message': response_message})
