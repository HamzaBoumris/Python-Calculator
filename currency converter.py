def currency_converter(amount, from_currency, to_currency):
    rates = {
        1: ("USD", 1.0),
        2: ("EUR", 0.91),
        3: ("MAD", 8.96),
    }

    if from_currency not in rates or to_currency not in rates:
        return "Currency not supported."

    from_code, from_rate = rates[from_currency]
    to_code, to_rate = rates[to_currency]
    amount_in_usd = amount / from_rate
    converted_amount = amount_in_usd * to_rate

    return round(converted_amount, 2), to_code

print("Currency Converter")
print("1: USD")
print("2: EUR")
print("3: MAD")

amount = float(input("Enter amount: "))
from_curr = int(input("From currency (1, 2, or 3): "))
to_curr = int(input("To currency (1, 2, or 3): "))

result, currency = currency_converter(amount, from_curr, to_curr)

if isinstance(result, str):
    print(result)

