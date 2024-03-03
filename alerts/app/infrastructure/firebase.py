import firebase_admin
from firebase_admin import credentials, messaging


class FirebaseClient:
    def __init__(self, service_account_key_path: str):
        cred = credentials.Certificate(service_account_key_path)
        firebase_admin.initialize_app(cred)

    def send_fcm_alert(self, device_registration_token: str or list, priority: str, title: str, message: str):
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=message,
            ),
            tokens=device_registration_token,
            android=messaging.AndroidConfig(
                priority=priority
            ),
        )

        response = messaging.send_each_for_multicast(message)
