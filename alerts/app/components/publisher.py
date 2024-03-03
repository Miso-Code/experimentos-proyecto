import os

from ..infrastructure.firebase import FirebaseClient
from ..services.alerts import AlertService

firebase_client = FirebaseClient("serviceAccountKey.json")
alerts_service = AlertService()


def send_alert(user_id: str, priority: str, title: str, message: str):
    user_devices = alerts_service.get_user_devices(user_id)
    test_token = os.getenv("TEST_FIREBASE_DEVICE_ID")
    if test_token:
        user_devices.append(test_token)
    firebase_client.send_fcm_alert(user_devices, priority, title, message)
