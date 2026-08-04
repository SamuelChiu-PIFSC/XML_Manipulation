import sys
import time
import xml.etree.ElementTree as ET

import pdfkit
from icecream import ic

import xml_utils


def search_xml(target_section: str, XML_FILE: str):
    ''' Searches for a specific section in the XML file and returns its parsed dictionary representation.

    args:
        target_section (str): The name of the section to search for in the XML file.
        XML_FILE (str): The path to the XML file to be searched.

    returns:
        dict: A dictionary representation of the found XML section, or None if the section is not found or an error occurs.
    '''

    try:
        
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        target = root.find(f".//{target_section}")

        if target is None:
            print(f"Warning: Section '{target_section}' not found in {XML_FILE}.")
            return None

        return xml_utils.xml_to_editable_dict(target)


    except Exception as e:
        print(f"Error occurred while searching for section: {e}")

        return None


if __name__ == "__main__":
    print("Test usage: searching for the item identification section in the XML file.")
    time.sleep(3)

    XML_FILE = "inport-xml.xml"
    target_section = "item-identification"
    result = search_xml(target_section, XML_FILE)

    print(f"Result for section '{target_section}':  \n\n\n  {result}")