import xml.etree.ElementTree as ET
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from models import ChatRequest, UpdateXMLRequest
from xml_utils import update_xml_file, xml_to_editable_dict

app = FastAPI()

XML_FILE = "inport-xml.xml"

# Locate main.py's folder dynamically
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/chat")
def chat(payload: ChatRequest):
    user_message = payload.message.strip().lower()

    target_section = None
    if (
        "item-identification" in user_message
        or "item identification" in user_message
    ):
        target_section = "item-identification"

    if target_section:
        try:
            tree = ET.parse(XML_FILE)
            root = tree.getroot()
            target = root.find(f".//{target_section}")

            if target is not None:
                parsed_dict = xml_to_editable_dict(target)
                return {
                    "is_prose": True,
                    "section_name": target_section,
                    "prose_dict": parsed_dict,
                }
        except Exception as e: # noqa: BLE001
            return {
                "is_prose": False,
                "reply": f"Error loading section: {e!s}",
            }

    return {
        "is_prose": False,
        "reply": f"Received: '{payload.message}'. Try clicking item-identification.",
    }


@app.post("/update")
def update(payload: UpdateXMLRequest):
    success, msg = update_xml_file(
        XML_FILE, payload.section_name, payload.updates
    )
    return {"success": success, "message": msg}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)