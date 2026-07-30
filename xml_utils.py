import xml.etree.ElementTree as ET


def xml_to_editable_dict(element: ET.Element) -> dict[str, str]:
    """Parses XML element children into key-value pairs."""
    data = {}
    for child in element:
        child_name = child.tag.replace("-", " ").replace("_", " ").title()
        val = child.text.strip() if child.text else ""
        data[child_name] = val
    return data


def update_xml_file(
    file_path: str, section_name: str, updates: dict[str, str]
) -> tuple[bool, str]:
    """Finds section and updates child elements with new values."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        clean_section = section_name.lower().replace(" ", "-")
        target = root.find(f".//{clean_section}")

        if target is None:
            target = root.find(f".//{clean_section.replace('-', '_')}")

        if target is not None:
            for child in target:
                child_name = (
                    child.tag.replace("-", " ").replace("_", " ").title()
                )
                if child_name in updates:
                    child.text = updates[child_name]

            # Save updated XML back to disk
            tree.write(file_path, encoding="utf-8", xml_declaration=True)
            return True, "XML file updated successfully!"

        return False, "Section not found."
    except Exception as e:
        return False, f"Failed to update XML: {e!s}"