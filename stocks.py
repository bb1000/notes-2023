import csv
import sys
import pathlib

this_code = sys.argv[0]

if len(sys.argv) < 2:
    print(f"Usage: {this_code} csv_file")
    exit()

csv_file = sys.argv[1]

if not pathlib.Path(csv_file).is_file():
    print(f'{csv_file} does not exist')
    exit()
    
csv_reader = csv.DictReader(open(csv_file))
shares = 0
for row in csv_reader:
    # convert the price data from string to float skipping the initial $ character (using [1:])
    closing_price_of_day = float(row['Close/Last'][1:])  
    if shares == 0:
        latest_price = closing_price_of_day # save the latest price from the first iteration
    shares_purchased = 1/closing_price_of_day
    shares += shares_purchased
    # print(shares_purchased, shares)

value = shares * latest_price
print(f'Total ({csv_file}) shares={round(shares, 3)} value={round(value, 2)}')