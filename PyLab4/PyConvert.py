import xml.etree.ElementTree as ET


def convert_xml(txt_file, xml_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    root = ET.Element("root")

    for line in lines:
        item = ET.SubElement(root, "item")
        item.text = line.strip()

    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

convert_xml('oldfile.txt', 'newxml.xml')