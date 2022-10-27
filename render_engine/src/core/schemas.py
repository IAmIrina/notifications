from pydantic import BaseModel


class Notification(BaseModel):
    email: str
    letter: str
    content_id: str
    user_id: str
    subject: str
    notification_id: str
