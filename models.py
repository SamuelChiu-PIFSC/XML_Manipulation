from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class UpdateXMLRequest(BaseModel):
    section_name: str
    updates: dict[str, str]  # e.g., {"Id": "12345", "Name": "New Name"}