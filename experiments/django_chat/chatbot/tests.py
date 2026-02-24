import json

from django.test import TestCase


class ChatbotEndpointsTests(TestCase):
    def test_chat_endpoint_returns_response(self):
        response = self.client.post(
            "/chatbot/chat/",
            data=json.dumps({"message": "hola"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("response", payload)

    def test_history_endpoint_returns_list(self):
        self.client.post(
            "/chatbot/chat/",
            data=json.dumps({"message": "primer mensaje"}),
            content_type="application/json",
        )

        response = self.client.get("/chatbot/history/")
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("history", payload)
        self.assertIsInstance(payload["history"], list)
