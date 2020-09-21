import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

url = "https://www.iban.com/currency-codes"


LIST = []

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

table = soup.find("table")
trs = table.find_all("tr")[1:]

for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    code = tds[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name': name.capitalize(),
                'code': code
            }
            LIST.append(country)


def question_a():
    print("Where are you from? Choose a country by number.")
    try:
        choice = int(input("#: "))
        if choice > len(LIST):
            print("Choose a number from the list.")
            question_a()
        else:
            country = LIST[choice]
            print(
                f"{country['name']}\n")
            name_a = country['name']
            code_a = country['code']
            question_b(name_a, code_a)
    except ValueError:
        print("That wasn't a number.")
        question_a()


def question_b(name_a, code_a):
    print("Now choose another country.")
    try:
        choice = int(input("#: "))
        if choice > len(LIST):
            print("Choose a number from the list.")
            question_b()
        else:
            country = LIST[choice]
            print(
                f"{country['name']}\n")
            name_b = country['name']
            code_b = country['code']
        exchange(code_a, code_b, name_a, name_b)
    except ValueError:
        print("That wasn't a number.")
        question_b(name_a, code_a)


def exchange(code_a, code_b, name_a, name_b):

    try:
        currency_amt = float(
            input(f"How many {code_a} do you wnat to convert to {code_b}\n"))
        url = f"https://transferwise.com/gb/currency-converter/{code_a}-to-{code_b}-rate?amount={currency_amt}"
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find("form").find("input")["value"]
        won = float(results)
        print(format_currency(currency_amt, code_a,
                              locale="ko_KR"), f"is ￦{currency_amt*won}")
    except ValueError:
        print("That wasn't a number.")


print("Hello! Please choose select a country by number:")
for index, country in enumerate(LIST):
    print(f"#{index} {country['name']}")

question_a()
