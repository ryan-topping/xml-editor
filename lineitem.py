import logging
import xml.etree.ElementTree as ET


class LineItem:
    def __init__(self, node: ET.Element):
        self._node = node

        self._part_number = self._node.find('PartNumber')
        self._tag = self._node.find('Tag')
        self._part_type = self._node.find('PartType')
        self._length = self._node.find('Length')
        self._unit_price = self._node.find('UnitPrice')
        self._quantity = self._node.find('Quantity')
        self._ext_price = self._node.find('ExtendedPrice')
    
    @property
    def part_number(self) -> str:
        return self._part_number.text
    
    @property
    def tag(self) -> str:
        return self._tag.text or '-'
    
    @property
    def part_type(self) -> str:
        return self._part_type.text
    
    @property
    def length(self) -> float:
        return float(self._length.text)
    
    @property
    def unit_price(self) -> float:
        return float(self._unit_price.text)
    
    @unit_price.setter
    def unit_price(self, value: float) -> None:
        self._unit_price.text = f'{value:.2f}'

    @property
    def quantity(self) -> int:
        return int(self._quantity.text)
    
    @property
    def ext_price(self) -> float:
        return float(self._ext_price.text)
    
    @ext_price.setter
    def ext_price(self, value: float) -> None:
        self._ext_price.text = f'{value:.2f}'

    def update_price(self, new_price: float) -> None:
        if self.length:
            new_price = new_price * self.length
        self.unit_price = round(new_price, 2)
        self.ext_price = round(self.unit_price * self.quantity, 2)

    def log_details(self, logger: logging.Logger, level: int = logging.INFO) -> None:
        logger.log(level, f'{self.tag:<2}  Part No.: {self.part_number}  Qty: {self.quantity}')

    def log_pricing(self, logger: logging.Logger, new: bool = False) -> None:
        logger.info(f'{"New:" if new else "Old:"} {self.unit_price:>10.2f}\t  Ext: {self.ext_price:>10.2f}')
        