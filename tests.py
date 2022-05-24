from unittest import TestCase, main
from backend.helper_functions import currency_converter, validate_currency


class TestValidateCurrecy(TestCase):

    def test_1_validate_currency(self):
        currency_code = 'USD'
        output = validate_currency(currency_code)
        self.assertEqual(output, True)

    def test_2_validate_currency(self):
        currency_code = 'USD1'
        output = validate_currency(currency_code)
        self.assertEqual(output, False)

    def test_3_validate_currency(self):
        currency_code = 'US$'
        output = validate_currency(currency_code)
        self.assertEqual(output, False)

    def test_4_validate_currency(self):
        currency_code = 'united state dollar'
        output = validate_currency(currency_code)
        self.assertEqual(output, False)

    def test_5_validate_currency(self):
        currency_code = '$'
        output = validate_currency(currency_code)
        self.assertEqual(output, False)


class TestCurrecyConverter(TestCase):

    def test_1_currency_converter(self):
        input_currency = 'usd'
        output_currency = 'usd'
        amount = 1
        rate = currency_converter(
            input_currency=input_currency, output_currency=output_currency, amount=amount)
        self.assertEqual(rate, '$ 1.0')

    def test_2_currency_converter(self):
        input_currency = 'usd'
        output_currency = 'usd'
        amount = 20
        rate = currency_converter(
            input_currency=input_currency, output_currency=output_currency, amount=amount)
        self.assertEqual(rate, '$ 20.0')

    def test_3_currency_converter(self):
        input_currency = 'inr'
        output_currency = 'inr'
        amount = 1
        rate = currency_converter(
            input_currency=input_currency, output_currency=output_currency, amount=amount)
        self.assertEqual(rate, '₹ 1.0')

    def test_4_currency_converter(self):
        input_currency = 'some fake currency code'
        output_currency = 'usd'
        amount = 1
        rate = currency_converter(
            input_currency=input_currency, output_currency=output_currency, amount=amount)
        self.assertEqual(
            rate, 'Currency rate not found! Please check the currency codes or amount.')


if __name__ == '__main__':
    main()
