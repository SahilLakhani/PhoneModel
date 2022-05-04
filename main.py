import math

if __name__ == '__main__':
    tax = 0.06
    disposal_fee = 12.75
    down_payment_percent = 0.14
    per_month = 24

    phone_name = input("Enter your phone model: ")
    base_price = float(input("Enter the base price of the phone: "))

    while base_price <= 0:
        print("Please enter a valid number! ")
        base_price = float(input("Enter the base price of the phone: "))

    warranty = float(input("Enter the cost of the warranty: "))

    while warranty <= 0:
        print("Please enter a valid number! ")
        warranty = float(input("Enter the cost of the warranty: "))

    tax_on_phone = (base_price + warranty) * tax
    total_cost = tax_on_phone + disposal_fee + base_price + warranty
    down_payment = (base_price + warranty) * down_payment_percent
    due_at_purchase = down_payment + tax_on_phone + disposal_fee
    finance_amount = base_price + warranty - down_payment
    payment_per_month = finance_amount / per_month

    print("Report:")
    print("Phone model name: " + phone_name)
    print('Base price: $' + format(base_price, '.2f'))
    print("Warranty cost: $" + format(warranty, '.2f'))
    print("Disposal fee: $" + format(disposal_fee, '.2f'))
    print("Sales tax: $" + format(tax_on_phone, '.2f'))
    print("Total cost: $" + format(total_cost, '.2f'))
    print("Down payment: $" + format(down_payment, '.2f'))
    print("Total amount due at purchase: $" + format(due_at_purchase, '.2f'))
    print("Finance amount: $" + format(finance_amount, '.2f'))
    print("Monthly payments: $" + format(payment_per_month, '.2f'))




