import os


class Config:
    SPORT_SESSION_URL = os.getenv('SPORT_SESSION_URL', 'http://localhost:5000/sport-sessions')
    ADVERSE_INCIDENTS_PROVIDER_URL = os.getenv('ADVERSE_INCIDENTS_PROVIDER_URL', 'http://localhost:8000/incidents')
    ADVERSE_INCIDENTS_PROVIDER_REFRESH_INTERVAL_SECONDS = int(
        os.getenv('ADVERSE_INCIDENTS_PROVIDER_REFRESH_INTERVAL_SECONDS', 600))
    ADVERSE_INCIDENTS_PROVIDER_API_KEY = os.getenv('ADVERSE_INCIDENTS_PROVIDER_API_KEY', '123')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    NOTIFICATION_SQS_QUEUE = os.getenv('NOTIFICATION_SQS_QUEUE', 'adverse_incidents_queue.fifo')
