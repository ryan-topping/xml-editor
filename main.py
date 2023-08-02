import pathlib
import xml.etree.ElementTree as ET


from dialogs import load_xml_file, save_xml_file
from pricelist import prices


file_path = load_xml_file()
path = pathlib.PurePath(file_path)
file_name = path.name
directory = path.parent

tree = ET.parse(file_path)
root = tree.getroot()

test = [item for item in root.findall('.//BOMTemplate')]

for node in test:
    part_number = node.find('PartNumber').text
    length = float(node.find('Length').text)
    unit_price_node = node.find('UnitPrice')
    unit_price = float(unit_price_node.text)
    quantity = int(node.find('Quantity').text)
    extended_price_node = node.find('ExtendedPrice')
    extended_price = float(extended_price_node.text)
    print(f'{part_number=} {unit_price=} {quantity=} {extended_price=}')
    new_price = prices.get(part_number, 0.0)
    if length:
        new_price = round(new_price * length, 2)
    new_extended_price = new_price * quantity
    unit_price_node.text = f'{new_price:.2f}'
    extended_price_node.text = f'{new_extended_price:.2f}'
    print(f'{new_price=:.2f} {new_extended_price=:.2f}')

new_file_path = save_xml_file(initialdir=directory, initialfile=file_name)

with open(new_file_path, 'w') as file:
    file.write(ET.tostring(root, encoding='unicode'))
