import csv


PRICE_FILE = 'pricelist.csv'


prices = {}
with open(PRICE_FILE, 'r') as file:
    csv_file = csv.reader(file)
    for part in csv_file:
        part_number, *_, price = part
        prices[part_number] = float(price)
