from decimal import Decimal, ROUND_HALF_UP
import locale
import decimal

locale.setlocale(locale.LC_ALL, '')  # Set the locale for currency formatting

MONTHS_IN_YEAR = 12
PERCENTAGE_DIVISOR = 100
CURRENCY_SYMBOL = locale.localeconv()['currency_symbol']

def calculate_interest(remaining_balance, annual_interest_rate):
    monthly_interest_rate = Decimal(annual_interest_rate) / PERCENTAGE_DIVISOR / MONTHS_IN_YEAR
    return remaining_balance * monthly_interest_rate

def make_payment(remaining_balance, monthly_payment, interest_paid):
    remaining_balance = remaining_balance + interest_paid
    remaining_balance -= monthly_payment
    return remaining_balance

def display_results(payment, interest_paid, remaining_balance):
    print(f"Платени: {format_currency(payment)} | Лихви: {format_currency(interest_paid)} | Остават: {format_currency(remaining_balance)}")

def handle_early_repayment(money_owed, payment, interest_paid):
    print(f"\nПоследното плащане е {format_currency(money_owed)}")
    print(f"Заемът ще бъде изплатен след 1 месец.")

def format_currency(amount):
    return locale.currency(amount, grouping=True)

def input_float(prompt):
    while True:
        try:
            return Decimal(input(prompt))
        except (ValueError, decimal.InvalidOperation):
            print("Грешка: Невалидно число. Моля въведете валидно число.")

def loan_repayment_calculator():
    try:
        money_owed = input_float("Колко пари дължиш в лева?\n")
        apr = input_float("Колко е годишният процент на лихва?\n")
        payment = input_float("Месечна вноска?\n")
        months = input_float("За какъв брой месеци да се покаже резултат?\n")

        # Check if values are non-negative
        if money_owed < Decimal(0) or apr < Decimal(0) or payment < Decimal(0) or months < Decimal(0):
            raise ValueError("Всички стойности трябва да са неотрицателни.")

        total_paid = Decimal(0)
        total_interest_paid = Decimal(0)

        for i in range(int(months)):
            interest_paid = calculate_interest(money_owed, apr)

            if money_owed - payment < Decimal(0):
                handle_early_repayment(money_owed, payment, interest_paid)
                break

            money_owed = make_payment(money_owed, payment, interest_paid)
            display_results(payment, interest_paid, money_owed)

            total_paid += payment
            total_interest_paid += interest_paid

        print_loan_summary(total_paid, total_interest_paid, money_owed, apr)

    except ValueError as e:
        print(f"Грешка: {e}")

def print_loan_summary(total_paid, total_interest_paid, remaining_balance, annual_interest_rate):
    print("\n=== КРАЙ НА ЗАЕМА ===")
    print(f"Общо заплатени: {format_currency(total_paid)}")
    print(f"Общо лихви: {format_currency(total_interest_paid)}")
    print(f"Оставаща сума: {format_currency(remaining_balance)}")
    print(f"Годишен процент на лихва: {annual_interest_rate}%")

if __name__ == "__main__":
    loan_repayment_calculator()
