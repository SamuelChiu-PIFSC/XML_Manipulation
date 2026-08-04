import xml.etree.ElementTree as ET


def xml_to_editable_dict(element: ET.Element) -> dict[str, str]:
    """Parses XML element children into key-value pairs."""
    data = {}
    for child in element:
        child_name = child.tag.replace("-", " ").replace("_", " ").title()
        val = child.text.strip() if child.text else ""
        data[child_name] = val
    return data

def search_xml(target_section: str, XML_FILE: str):
    ''' Searches for a specific section in the XML file and returns its parsed dictionary representation.

    args:
        target_section (str): The name of the section to search for in the XML file.
        XML_FILE (str): The path to the XML file to be searched.

    returns:
        dict: A dictionary representation of the found XML section, or None if the section is not found or an error occurs.
    '''  # noqa: E501

    try:
        
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        target = root.find(f".//{target_section}")

        if target is None:
            print(f"Warning: Section '{target_section}' not found in {XML_FILE}.")
            return None

        return xml_to_editable_dict(target)


    except Exception as e:
        print(f"Error occurred while searching for section: {e}")

        return None

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

    