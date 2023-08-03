import dialogs
import lineitem
import log
import logging
import os
import pricelist
import xml.etree.ElementTree as ET


def main():
    bom_file_path = dialogs.load_xml_file()
    if not bom_file_path:
        return
    
    bom_directory, bom_full_file_name = os.path.split(bom_file_path)

    new_file_path = dialogs.save_xml_file(
        initialdir=bom_directory, 
        initialfile=bom_full_file_name
    )
    if not new_file_path:
        return

    new_directory, new_full_file_name = os.path.split(new_file_path)
    new_file_name, new_extension = os.path.splitext(new_full_file_name)

    logger_file_path = f'{new_directory}\{new_file_name}.log'
    logger = log.get_logger(logger_file_path)

    logger.info('--- START ---')
    logger.info(f'BOM File Path:  {bom_file_path}')
    logger.info(f'New File Path:  {new_file_path}')
    logger.info('Parsing Bill of Materials')

    try:
        tree = ET.parse(bom_file_path)
    except ET.ParseError:
        logger.critical('XML file problem.')
        return
    
    root = tree.getroot()
    bill_of_materials = [line_item for line_item in root.findall('.//BOMTemplate')]

    logger.info(f'Total line items: {len(bill_of_materials)}')

    success_count = 0
    fail_count = 0
    skipped: list[lineitem.LineItem] = []

    for line_item in bill_of_materials:
        item = lineitem.LineItem(line_item)
        item.log_details(logger)
        item.log_pricing(logger)

        new_price = pricelist.prices.get(item.part_number, None)

        if new_price is None:
            logger.warning('Part not found in the price list.')
            fail_count += 1
            skipped.append(item)
            continue

        item.update_price(new_price)
        item.log_pricing(logger, new=True)

        success_count += 1

    with open(new_file_path, 'w') as file:
        file.write(ET.tostring(root, encoding='unicode'))

    logger.info(f'Successful lines items: {success_count}')
    
    if skipped:
        logger.warning(f'Skipped line items: {fail_count}')
        for item in skipped:
            item.log_details(logger, logging.WARN)


if __name__ == '__main__':
    main()
