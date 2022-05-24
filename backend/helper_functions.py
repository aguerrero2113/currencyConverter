from forex_python.converter import (
    CurrencyRates,
    CurrencyCodes
)


def validate_currency(currency_code):
    return (len(currency_code) == 3 and currency_code.isalpha())


def currency_converter(input_currency, output_currency, amount):
    try:
        c = CurrencyRates()
        if validate_currency(input_currency) and validate_currency(output_currency):
            rate = round(c.convert(input_currency.upper(),
                         output_currency.upper(), amount), 2)
            c = CurrencyCodes()
            symbol = c.get_symbol(output_currency.upper())
            if symbol:
                return f'{symbol} {rate}'
        return rate
    except Exception as error:
        print("############################ ERROR ############################")
        print(error)
        print("###############################################################")
        return 'Currency rate not found! Please check the currency codes or amount.'
