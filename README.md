
# Live Editable XML Document Assistant

A FastAPI-based web application designed for loading, viewing, and modifying structured InPort XML documentation in real-time through an interactive chat interface.

---

## Features

* **Interactive XML Parsing:** Search and target specific sections (e.g., `item-identification`) directly from the input interface.
* **Live In-Browser Editing:** Dynamically load XML attributes into content-editable cards and submit updates directly to disk.
* **Template Generation:** Utility script to process full XML files into condensed, reusable prototype templates.
* **FastAPI Backend:** Lightweight REST server serving modern dark-themed UI frontend.

---

## Directory Structure

```text
XML_Manipulation/
│
├── static/
│   ├── index.html                  # Frontend chat UI and dynamic editor script
│   └── styles.css                  # Dark-theme styling rules
│
├── xml_template/
│   ├── condensed_template.xml      # Auto-generated prototype XML structure
│   └── xml_template_generator.py   # Script for condensing repeating XML elements
│
├── inport-xml.xml                  # Main InPort XML target document
├── main.py                         # FastAPI web application routes
├── models.py                       # Pydantic schema models for requests
├── xml_utils.py                    # Helper functions for parsing and updating XML
├── pyproject.toml / uv.lock        # Package management and project metadata
└── README.md                       # Project documentation

```

---

## File Descriptions

**Core Backend & API**
* `main.py`: Serves static web pages and handles `/chat` (querying) and `/update` (saving updates) endpoints.
* `models.py`: Defines `ChatRequest` and `UpdateXMLRequest` payload contracts using Pydantic.
* `xml_utils.py`: Performs XML traversal, converting nodes into key-value dictionaries and writing edits back to the XML file.


**Frontend UI**

* `static/index.html`: Web interface providing real-time dynamic card rendering for content editable fields.


* `static/styles.css`: Custom CSS providing dark mode styling and input form components.


**Template Utilities**

* `xml_template/xml_template_generator.py`: Generates representative skeleton templates by collapsing repeating XML child tags into merged prototypes.


---

## Getting Started

### Prerequisites

Make sure Python is installed on your machine. Dependencies are managed via standard Python packages or `uv`.

### Installation & Running

1. **Install Dependencies**
Ensure `fastapi`, `uvicorn`, and `pydantic` are installed.


2. **Launch the Server**
Run the application using `uvicorn` or execute `main.py` directly:


```bash
python main.py

```
The application will launch on `http://127.0.0.1:8000`.


3. **Usage**
* Open `http://127.0.0.1:8000` in your web browser.

* Click or enter **`item-identification`** in the prompt area to load the editable card.

* Modify the fields inside the editor block and click **Save Changes to XML** to persist modifications.


---

## Generating XML Templates

To create a clean skeleton prototype from a massive XML file, run:

```bash
python xml_template/xml_template_generator.py

```

This produces `condensed_template.xml` with placeholder text flags while maintaining the valid structure.
