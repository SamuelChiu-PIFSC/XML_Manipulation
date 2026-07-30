import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

TEXT_FLAG = "[EMPTY_VALUE]"
ATTR_FLAG = "[EMPTY_ATTRIBUTE]"

def create_condensed_template(node):
    new_node = ET.Element(node.tag)
    
    # Process attributes
    for attr_key, attr_val in node.attrib.items():
        if attr_key.startswith("xmlns") or attr_key == "version":
            new_node.attrib[attr_key] = attr_val
        else:
            new_node.attrib[attr_key] = ATTR_FLAG

    if len(node) == 0:
        if node.text and node.text.strip():
            new_node.text = TEXT_FLAG
    else:
        # Group children by tag name to merge structure across repeating siblings
        tag_groups = {}
        for child in node:
            tag_groups.setdefault(child.tag, []).append(child)
            
        for tag, instances in tag_groups.items():
            if len(instances) == 1:
                new_node.append(create_condensed_template(instances[0]))
            else:
                # Merge repeating sibling elements into a single robust prototype
                merged_prototype = ET.Element(tag)
                # Combine all unique child elements across all instances
                seen_subtags = set()
                for inst in instances:
                    # Collect attributes
                    for k, v in inst.attrib.items():
                        merged_prototype.attrib[k] = ATTR_FLAG
                    # Collect child elements
                    for subchild in inst:
                        if subchild.tag not in seen_subtags:
                            seen_subtags.add(subchild.tag)
                            merged_prototype.append(create_condensed_template(subchild))
                new_node.append(merged_prototype)
                
    return new_node

def generate_smart_xml_template(input_filepath, output_filepath):
    # Register namespaces prior to parsing so standard ET doesn't discard them
    ET.register_namespace('xs', 'http://www.w3.org/2001/XMLSchema')
    
    tree = ET.parse(input_filepath)
    root = tree.getroot()
    
    template_root = create_condensed_template(root)
    
    rough_string = ET.tostring(template_root, encoding='utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="   ")
    
    clean_xml = "\n".join([line for line in pretty_xml.splitlines() if line.strip()])

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(clean_xml)

    print(f"Clean, comprehensive prototype template created at: {output_filepath}")

if __name__ == "__main__":
    generate_smart_xml_template("inport-xml.xml", "condensed_template.xml")