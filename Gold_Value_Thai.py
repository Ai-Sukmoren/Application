import requests
from bs4 import BeautifulSoup

url = "https://www.goldtraders.or.th/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Find the element with the specific tag and attribute
value_element = soup.find(style="text-align:right;vertical-align:middle;")


if value_element:
    value = value_element.text
    value = value.replace('\n','')
    value = value.replace(',','')
    value = round(float(value))
    print(f"the current value of gold is {value} Bath")
else:
    print("value not found")


def unit_of_gold():
    quantity = input('Unit of gold: ')
    try:
        if '.' in quantity:
            return float(quantity)
        else:
            return int(quantity)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

def currrent_value_of_your_gold(unit,gold_value = value):
    value = unit * gold_value
    print(f'Your {unit} unit of gold value is {value}')


unit = unit_of_gold()

currrent_value_of_your_gold(unit)